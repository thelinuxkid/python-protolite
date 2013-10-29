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


def encode_struct(num, fmt):
    values = struct.pack(fmt, num)
    return [ord(v) for v in values]


def decode_struct(data, index, bits, fmt):
    last = index
    index += bits
    values = [chr(i) for i in data[last:index]]
    values = ''.join(values)
    num = struct.unpack(fmt, values)
    return num[0], index


def decode_key(key):
    "return a tuple containing the field and the wire type"

    return key >> 3, key & 7


def encode_key(field, wire):
    "return the encoded field and wire type"

    return (field << 3) | wire


def decode_varint(data, index):
    "return an int32, int64, uint32, uint64, sint32, sint64, bool, or enum"

    item = 128
    num = 0
    left = 0
    while item & 128:
        item = data[index]
        index += 1
        value = (item & 127) << left
        num += value
        left += 7
    return num, index


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


def decode_delimited(data, index):
    "return a string, bytes, embedded messages, or packed repeated fields"

    length, index = decode_varint(data, index)
    last = index
    index += length
    res = data[last:index]
    return res, index


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
    while index < length:
        value, index = decode_varint(data, index)
        field, wire = decode_key(value)
        if field not in proto:
            continue
        info = proto[field]
        _type = info['type']
        name = info['name']
        if wire == 0:
            # TODO support int32, int64, uint32, uint64, sint32, sint64
            num, index = decode_varint(data, index)
            if _type == 'bool':
                num = bool(num)
            if _type == 'enum':
                num = info['message'][num]
            msg[name] = num
            continue
        if wire == 1:
            fmt = struct_formats[_type]
            num, index = decode_struct(data, index, 8, fmt)
            msg[name] = num
            continue
        if wire == 2:
            # TODO support bytes and packed repeated fields
            item, index = decode_delimited(data, index)
            if _type == 'embedded':
                msg[name] = _decode(info['message'], item)
            if _type == 'string':
                msg[name] = ''.join([chr(i) for i in item])
            if _type == 'repeated':
                if name not in msg:
                    msg[name] = []
                msg[name].append(_decode(info['message'], item))
            continue
        if wire == 5:
            fmt = struct_formats[_type]
            num, index = decode_struct(data, index, 4, fmt)
            msg[name] = num
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
            key = encode_key(field, 0)
            key = encode_varint(key)
            if _type == 'enum':
                value = encode_varint(v)
            if _type == 'bool':
                value = encode_varint(int(v))
            if _type in varints:
                value = encode_varint(v)
            data += key + value
            continue
        if _type in _64bit_types:
            key = encode_key(field, 1)
            key = encode_varint(key)
            fmt = struct_formats[_type]
            value = encode_struct(v, fmt)
            data += key + value
            continue
        if _type in delimited_types:
            # TODO support bytes and packed repeated fields
            key = encode_key(field, 2)
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
            key = encode_key(field, 5)
            key = encode_varint(key)
            fmt = struct_formats[_type]
            value = encode_struct(v, fmt)
            data += key + value
            continue
    return data
