import struct

varint_types = [
    'int32',
    'int64',
    'uint32',
    'uint64',
    'sint32',
    'sint64',
    'bool',
    'enum',
]
unsigned_varint_types = [
    'uint32',
    'uint64',
]
_64bit_types = ['fixed64', 'sfixed64', 'double']
delimited_types = ['string', 'bytes', 'embedded', 'packed']
_32bit_types = ['fixed32', 'sfixed32', 'float']
struct_formats = dict([
    ('fixed64', '<Q'),
    ('sfixed64', '<q'),
    ('double', '<d'),
    ('fixed32', '<I'),
    ('sfixed32', '<i'),
    ('float', '<f'),
])
joinstr = ''.join


def decode(proto, data):
    data = [ord(d) for d in data]
    return _decode(proto, data)


def _decode(proto, data):
    index = 0
    length = len(data)
    msg = dict()
    while index < length:
        # optimization: avoid function calls to decode_varint, decode_key
        item = 128
        key = 0
        left = 0
        while item & 128:
            item = data[index]
            index += 1
            value = (item & 127) << left
            key += value
            left += 7
        field = key >> 3
        wire = key & 7
        # end optimization
        if field not in proto:
            continue
        info = proto[field]
        _type = info['type']
        repeated = info['scope'] == 'repeated'
        name = info['name']
        if repeated and name not in msg:
            msg[name] = list()
        if wire == 0:
            # TODO support int32, int64, uint32, sint32, sint64
            # optimization: avoid function call to decode_varint
            item = 128
            num = 0
            left = 0
            while item & 128:
                item = data[index]
                index += 1
                value = (item & 127) << left
                num += value
                left += 7
            # end optimization
            if _type == 'bool':
                num = bool(num)
            if repeated:
                msg[name].append(num)
                continue
            msg[name] = num
            continue
        if wire == 1:
            fmt = struct_formats[_type]
            # optimization: avoid function call to decode_struct
            last = index
            index += 8
            values = [chr(i) for i in data[last:index]]
            values = joinstr(values)
            num = struct.unpack(fmt, values)
            # end optimization
            if repeated:
                msg[name].append(num[0])
                continue
            msg[name] = num[0]
            continue
        if wire == 2:
            # TODO support bytes and packed repeated fields
            # optimization: avoid function call to decode_delimited
            item = 128
            _length = 0
            left = 0
            while item & 128:
                item = data[index]
                index += 1
                value = (item & 127) << left
                _length += value
                left += 7
            last = index
            index += _length
            item = data[last:index]
            # end optimization
            if _type == 'embedded':
                item = _decode(info['message'], item)
                if repeated:
                    msg[name].append(item)
                    continue
                msg[name] = item
            if _type == 'string':
                item = joinstr([chr(i) for i in item])
                # TODO: need to think through unicode more completely
                item = item.decode('utf8')
                if repeated:
                    msg[name].append(item)
                    continue
                msg[name] = item
            continue
        if wire == 5:
            fmt = struct_formats[_type]
            # optimization: avoid function call to decode_struct
            last = index
            index += 4
            values = [chr(i) for i in data[last:index]]
            values = ''.join(values)
            num = struct.unpack(fmt, values)
            # end optimization
            if repeated:
                msg[name].append(num[0])
                continue
            msg[name] = num[0]
            continue
        raise ValueError(
            'invalid wire type: {wire}'.format(wire=wire)
        )
    return msg


def encode(proto, msg):
    data = _encode(proto, msg)
    data = [chr(d) for d in data]
    return ''.join(data)


def _encode(proto, msg):
    data = []
    for k, values in msg.items():
        info = proto[k]
        field = info['field']
        _type = info['type']
        repeated = info['scope'] == 'repeated'
        if _type in varint_types:
            if repeated:
                for v in values:
                    if _type in unsigned_varint_types and v < 0:
                        raise ValueError(
                            '{_type} value cannot be negative: {v}'.format(
                                _type=_type,
                                v=v,
                            )
                        )
                    # TODO support int32, int64, uint32, sint32, sint64
                    # optimization: avoid function calls to encode_key
                    key = (field << 3) | 0
                    # end optimization
                    # optimization: avoid function calls to encode_varint
                    _next = 1
                    _value = key
                    key = []
                    while _next:
                        _next = _value >> 7
                        shift = 128 if _next else 0
                        part = (_value & 127) | shift
                        key.append(part)
                        _value = _next
                    # end optimization
                    if _type == 'bool':
                        v = int(v)
                    # optimization: avoid function calls to encode_varint
                    _next = 1
                    _value = v
                    values = []
                    while _next:
                        _next = _value >> 7
                        shift = 128 if _next else 0
                        part = (_value & 127) | shift
                        values.append(part)
                        _value = _next
                    data += key + values
                continue
            v = values
            if _type in unsigned_varint_types and v < 0:
                raise ValueError(
                    '{_type} value cannot be negative: {v}'.format(
                        _type=_type,
                        v=v,
                    )
                )
            # TODO support int32, int64, uint32, sint32, sint64
            # optimization: avoid function calls to encode_key
            key = (field << 3) | 0
            # end optimization
            # optimization: avoid function calls to encode_varint
            _next = 1
            _value = key
            key = []
            while _next:
                _next = _value >> 7
                shift = 128 if _next else 0
                part = (_value & 127) | shift
                key.append(part)
                _value = _next
            # end optimization
            if _type == 'bool':
                v = int(v)
            # optimization: avoid function calls to encode_varint
            _next = 1
            _value = v
            values = []
            while _next:
                _next = _value >> 7
                shift = 128 if _next else 0
                part = (_value & 127) | shift
                values.append(part)
                _value = _next
            data += key + values
            continue
        if _type in _64bit_types:
            if repeated:
                for v in values:
                    # optimization: avoid function calls to encode_key
                    key = (field << 3) | 1
                    # end optimization
                    # optimization: avoid function calls to encode_varint
                    _next = 1
                    _value = key
                    key = []
                    while _next:
                        _next = _value >> 7
                        shift = 128 if _next else 0
                        part = (_value & 127) | shift
                        key.append(part)
                        _value = _next
                    # end optimization
                    fmt = struct_formats[_type]
                    # optimization: avoid function call to encode_struct
                    value = [ord(b) for b in struct.pack(fmt, v)]
                    # end optimization
                    data += key + value
                continue
            v = values
            # optimization: avoid function calls to encode_key
            key = (field << 3) | 1
            # end optimization
            # optimization: avoid function calls to encode_varint
            _next = 1
            _value = key
            key = []
            while _next:
                _next = _value >> 7
                shift = 128 if _next else 0
                part = (_value & 127) | shift
                key.append(part)
                _value = _next
            # end optimization
            fmt = struct_formats[_type]
            # optimization: avoid function call to encode_struct
            value = [ord(b) for b in struct.pack(fmt, v)]
            # end optimization
            data += key + value
            continue
        if _type in delimited_types:
            if repeated:
                for v in values:
                    # TODO support bytes and packed repeated fields
                    # optimization: avoid function calls to encode_key
                    key = (field << 3) | 2
                    # end optimization
                    # optimization: avoid function calls to encode_varint
                    _next = 1
                    _value = key
                    key = []
                    while _next:
                        _next = _value >> 7
                        shift = 128 if _next else 0
                        part = (_value & 127) | shift
                        key.append(part)
                        _value = _next
                    # end optimization
                    if _type == 'embedded':
                        value = _encode(info['message'], v)
                        length = len(value)
                        # optimization: avoid function calls to encode_varint
                        _next = 1
                        _value = length
                        length = []
                        while _next:
                            _next = _value >> 7
                            shift = 128 if _next else 0
                            part = (_value & 127) | shift
                            length.append(part)
                            _value = _next
                        # end optimization
                        data += key + length + value
                    if _type == 'string':
                        # optimization: avoid function calls to
                        # encode_delimited
                        length = len(v)
                        # optimization: avoid function calls to encode_varint
                        _next = 1
                        _value = length
                        length = []
                        while _next:
                            _next = _value >> 7
                            shift = 128 if _next else 0
                            part = (_value & 127) | shift
                            length.append(part)
                            _value = _next
                        # end optimization
                        value = [ord(i) for i in v]
                        data += key + length + value
                        # end optimization
                continue

            # TODO: need to handle unicode more completely
            if isinstance(values, unicode):
                values = values.encode('utf8')

            v = values
            # TODO support bytes and packed repeated fields
            # optimization: avoid function calls to encode_key
            key = (field << 3) | 2
            # end optimization
            # optimization: avoid function calls to encode_varint
            _next = 1
            _value = key
            key = []
            while _next:
                _next = _value >> 7
                shift = 128 if _next else 0
                part = (_value & 127) | shift
                key.append(part)
                _value = _next
            # end optimization
            if _type == 'embedded':
                value = _encode(info['message'], v)
                length = len(value)
                # optimization: avoid function calls to encode_varint
                _next = 1
                _value = length
                length = []
                while _next:
                    _next = _value >> 7
                    shift = 128 if _next else 0
                    part = (_value & 127) | shift
                    length.append(part)
                    _value = _next
                # end optimization
                data += key + length + value
            if _type == 'string':
                # optimization: avoid function calls to encode_delimited
                length = len(v)
                # optimization: avoid function calls to encode_varint
                _next = 1
                _value = length
                length = []
                while _next:
                    _next = _value >> 7
                    shift = 128 if _next else 0
                    part = (_value & 127) | shift
                    length.append(part)
                    _value = _next
                # end optimization
                value = [ord(i) for i in v]
                data += key + length + value
                # end optimization
            continue
        if _type in _32bit_types:
            if repeated:
                for v in values:
                    # optimization: avoid function calls to encode_key
                    key = (field << 3) | 5
                    # end optimization
                    # optimization: avoid function calls to encode_varint
                    _next = 1
                    _value = key
                    key = []
                    while _next:
                        _next = _value >> 7
                        shift = 128 if _next else 0
                        part = (_value & 127) | shift
                        key.append(part)
                        _value = _next
                    # end optimization
                    fmt = struct_formats[_type]
                    # optimization: avoid function call to encode_struct
                    value = [ord(b) for b in struct.pack(fmt, v)]
                    # end optimization
                    data += key + value
                continue
            v = values
            # optimization: avoid function calls to encode_key
            key = (field << 3) | 5
            # end optimization
            # optimization: avoid function calls to encode_varint
            _next = 1
            _value = key
            key = []
            while _next:
                _next = _value >> 7
                shift = 128 if _next else 0
                part = (_value & 127) | shift
                key.append(part)
                _value = _next
            # end optimization
            fmt = struct_formats[_type]
            # optimization: avoid function call to encode_struct
            value = [ord(b) for b in struct.pack(fmt, v)]
            # end optimization
            data += key + value
            continue
    return data
