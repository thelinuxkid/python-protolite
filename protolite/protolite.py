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
varints = ['int32', 'int64', 'uint32', 'uint64', 'sint32', 'sint64']
_64bit_types = ['fixed64', 'sfixed64', 'double']
delimited_types = ['string', 'bytes', 'embedded', 'packed', 'repeated']
_32bit_types = ['fixed32', 'sfixed32', 'float']

struct_formats = dict([
    ('fixed64', '<Q'),
    ('sfixed64', '<q'),
    ('double', '<d'),
    ('fixed32', '<I'),
    ('sfixed32', '<i'),
    ('float', '<f'),
])


def encode_varint(num):
    "return an encoded int32, int64, uint32, uint64, sint32, sint64, bool, or enum"

    value =  num & 127
    _next = (num & (127 << 7)) >> 7
    shift = 14
    values = []
    while _next:
        values.append(value | 128)
        value = _next
        _next = (num & (127 << shift)) >> shift
        shift += 7
    values.append(value)
    return values


def encode_delimited(item):
    "return an encoded string, bytes, embedded messages, or packed repeated fields"

    length = len(item)
    length = encode_varint(length)
    data = [ord(i) for i in item]
    return length + data


def decode(proto, data):
    data = [ord(d) for d in data]
    return _decode(proto, data)


def _decode(proto, data):
    index = 0
    length = len(data)
    msg = dict()
    # optmization: use local variable inside function
    join = ''.join
    # end optimization
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
        name = info['name']
        if wire == 0:
            # TODO support int32, int64, uint32, uint64, sint32, sint64
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
            msg[name] = num
            continue
        if wire == 1:
            fmt = struct_formats[_type]
            # optimization: avoid function call to decode_struct
            last = index
            index += 8
            values = [chr(i) for i in data[last:index]]
            values = ''.join(values)
            num = struct.unpack(fmt, values)
            msg[name] = num[0]
            # end optimization
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
                msg[name] = _decode(info['message'], item)
            if _type == 'string':
                msg[name] = join([chr(i) for i in item])
            if _type == 'repeated':
                if name not in msg:
                    msg[name] = []
                msg[name].append(_decode(info['message'], item))
            continue
        if wire == 5:
            fmt = struct_formats[_type]
            # optimization: avoid function call to decode_struct
            last = index
            index += 4
            values = [chr(i) for i in data[last:index]]
            values = ''.join(values)
            num = struct.unpack(fmt, values)
            msg[name] = num[0]
            # end optimization
            continue
        raise ValueError(
          'invalid wire type: {wire}'.format(wire=wire)
        )
    return msg


def encode(proto, msg):
    data = _encode(proto, msg)
    data = [chr(d) for d in data]
    return  ''.join(data)


def _encode(proto, msg):
    data =  []
    for k,v in msg.items():
        info = proto[k]
        field = info['field']
        _type = info['type']
        if _type in varint_types:
            # TODO support int32, int64, uint32, uint64, sint32, sint64
            # optimization: avoid function calls to encode_key
            key = (field << 3) | 0
            # end optimization
            key = encode_varint(key)
            if _type == 'bool':
                v = int(v)
            value = encode_varint(v)
            data += key + value
            continue
        if _type in _64bit_types:
            # optimization: avoid function calls to encode_key
            key = (field << 3) | 1
            # end optimization
            key = encode_varint(key)
            fmt = struct_formats[_type]
            # optimization: avoid function call to encode_struct
            value = [ord(b) for b in struct.pack(fmt, v)]
            # end optimization
            data += key + value
            continue
        if _type in delimited_types:
            # TODO support bytes and packed repeated fields
            # optimization: avoid function calls to encode_key
            key = (field << 3) | 2
            # end optimization
            key = encode_varint(key)
            if _type == 'embedded':
                value = _encode(info['message'], v)
                length = encode_varint(len(value))
                data += key + length + value
            if _type == 'string':
                value = encode_delimited(v)
                data += key + value
            if _type == 'repeated':
                for d in v:
                    value = _encode(info['message'], d)
                    length = encode_varint(len(value))
                    data += key + length + value
            continue
        if _type in _32bit_types:
            # optimization: avoid function calls to encode_key
            key = (field << 3) | 5
            # end optimization
            key = encode_varint(key)
            fmt = struct_formats[_type]
            # optimization: avoid function call to encode_struct
            value = [ord(b) for b in struct.pack(fmt, v)]
            # end optimization
            data += key + value
            continue
    return data
