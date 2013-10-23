from nose.tools import eq_ as equal

from protolite import protolite


class decoding(object):
    message_foo = dict([
        (1, dict([
            ('type', 'string'),
            ('name', 'body'),
        ])),
    ])
    bar_type = dict([
        (4, 'text'),
    ])
    message_bar = dict([
        (1, dict([
            ('type', 'enum'),
            ('name', 'type'),
            ('message', bar_type),
        ])),
        (4, dict([
            ('type', 'embedded'),
            ('name', 'message_foo'),
            ('message', message_foo),
        ])),
    ])
    message_baz = dict([
        (1, dict([
            ('type', 'embedded'),
            ('name', 'message_bar'),
            ('message', message_bar),
        ])),
        (3, dict([
            ('type', 'uint64'),
            ('name', 'baz_id'),
        ])),
    ])
    sna_type = dict([
        (8, 'message_baz'),
    ])
    message_sna = dict([
        (1, dict([
            ('type', 'enum'),
            ('name', 'type'),
            ('message', sna_type),
        ])),
        (8, dict([
            ('type', 'embedded'),
            ('name', 'message_baz'),
            ('message', message_baz),
        ])),
    ])
    foo = dict([
        (1, dict([
            ('type', 'uint64'),
            ('name', 'foo_id'),
        ])),
    ])
    bar = dict([
        (1, dict([
            ('type', 'uint64'),
            ('name', 'bar_id'),
        ])),
        (5, dict([
            ('type', 'repeated'),
            ('name', 'foos'),
            ('message', foo)
        ])),
    ])


class encoding(object):
    message_foo = dict([
        ('body', dict([
            ('type', 'string'),
            ('field', 1),
        ])),
    ])
    bar_type = dict([
        ('text', 4),
    ])
    message_bar = dict([
        ('type', dict([
            ('type', 'enum'),
            ('field', 1),
            ('message', bar_type),
        ])),
        ('message_foo', dict([
            ('type', 'embedded'),
            ('field', 4),
            ('message', message_foo),
        ])),
    ])
    message_baz = dict([
        ('message_bar', dict([
            ('type', 'embedded'),
            ('field', 1),
            ('message', message_bar),
        ])),
        ('baz_id', dict([
            ('type', 'uint64'),
            ('field', 3),
        ])),
    ])
    foo = dict([
        ('foo_id', dict([
            ('type', 'uint64'),
            ('field', 1),
        ])),
    ])
    bar = dict([
        ('bar_id', dict([
            ('type', 'uint64'),
            ('field', 1),
        ])),
        ('foos', dict([
            ('type', 'repeated'),
            ('field', 5),
            ('message', foo)
        ])),
    ])
    sna_type = dict([
        ('message_baz', 8),
    ])
    message_sna = dict([
        ('type', dict([
            ('type', 'enum'),
            ('field', 1),
            ('message', sna_type),
        ])),
        ('message_baz', dict([
            ('type', 'embedded'),
            ('field', 8),
            ('message', message_baz),
        ])),
    ])


def test_decode_key_simple():
    field, wire = protolite.decode_key(8)
    equal(1, field)
    equal(0, wire)


def test_encode_key_simple():
    key = protolite.encode_key(1,0)
    equal(8, key)


def test_decode_varint_simple():
    value, index = protolite.decode_varint([168, 172, 2], 0)
    equal(38440, value)
    equal(3, index)


def test_encode_varint_simple():
    value = protolite.encode_varint(38440)
    equal([168, 172, 2], value)


def test_decode_32bit_simple():
    value, index = protolite.decode_struct(
        [47, 201, 244, 194],
        0,
        4,
        '<f',
    )
    equal(-122.39293670654297, value)
    equal(4, index)


def test_encode_32bit_simple():
    value = protolite.encode_struct(-122.39293670654297, '<f')
    equal([47, 201, 244, 194], value)


def test_decode_64bit_simple():
    value, index = protolite.decode_struct(
        [0, 0, 0, 224, 37, 153, 94, 192],
        0,
        8,
        '<d',
    )
    equal(-122.39293670654297, value)
    equal(8, index)


def test_encode_64bit_simple():
    value = protolite.encode_struct(-122.39293670654297, '<d')
    equal([0, 0, 0, 224, 37, 153, 94, 192], value)


def test_decode_delimited_simple():
    data = [7, 116, 101, 115, 116, 105, 110, 103]
    value, index = protolite.decode_delimited(data, 0)
    equal([116, 101, 115, 116, 105, 110, 103], value)
    equal(8, index)


def test_encode_delimited_simple():
    value = protolite.encode_delimited('testing')
    want = [7, 116, 101, 115, 116, 105, 110, 103]
    equal(want, value)


def test_decode_embedded():
    data = '\x08\x08B\x12\n\r\x08\x04"\t\n\x07foobody\x18\xb9`'
    msg = protolite.decode(decoding.message_sna, data)
    want =  dict([
        ('message_baz', dict([
            ('baz_id', 12345),
            ('message_bar', dict([
                ('message_foo', dict([
                    ('body', 'foobody'),
                ])),
                ('type', 'text'),
            ])),
        ])),
        ('type', 'message_baz'),
    ])
    equal(want, msg)


def test_encode_embedded():
    # Don't check against data string since protolite doesn't use OrderedDict
    msg =  dict([
        ('message_baz', dict([
            ('baz_id', 12345),
            ('message_bar', dict([
                ('message_foo', dict([
                    ('body', 'foobody'),
                ])),
                ('type', 'text'),
            ])),
        ])),
        ('type', 'message_baz'),
    ])
    data = protolite.encode(encoding.message_sna, msg)
    res = protolite.decode(decoding.message_sna, data)
    equal(msg, res)


def test_decode_repeated():
    data = '\x08\n*\x02\x08\n*\x02\x08\x14'
    msg = protolite.decode(decoding.bar, data)
    want = dict([
      ('bar_id', 10),
      ('foos', [
        dict([('foo_id', 10)]),
        dict([('foo_id', 20)]),
      ]),
    ])
    equal(want, msg)


def test_encode_repeated():
    # Don't check against data string since protolite doesn't use OrderedDict
    msg = dict([
      ('bar_id', 10),
      ('foos', [
        dict([('foo_id', 10)]),
        dict([('foo_id', 20)]),
      ]),
    ])
    data = protolite.encode(encoding.bar, msg)
    res = protolite.decode(decoding.bar, data)
    equal(msg, res)

def test_decode_bool_simple():
    proto = dict([
        (7, dict([
            ('type', 'bool'),
            ('name', 'is_foo'),
        ])),
    ])
    data = '8\x00'
    msg = protolite.decode(proto, data)
    want = dict([('is_foo', False)])
    equal(want, msg)


def test_encode_bool_simple():
    # Don't check against data string since protolite doesn't use OrderedDict
    enc_proto = dict([
        ('is_foo', dict([
            ('type', 'bool'),
            ('field', 7),
        ])),
    ])
    dec_proto = dict([
        (7, dict([
            ('type', 'bool'),
            ('name', 'is_foo'),
        ])),
    ])
    msg = dict([('is_foo', False)])
    data = protolite.encode(enc_proto, msg)
    res = protolite.decode(dec_proto, data)
    equal(msg, res)


def test_decode_enum_simple():
    _type = dict([
        (7, 'msg-type'),
    ])
    proto = dict([
        (7, dict([
            ('type', 'enum'),
            ('name', 'type'),
            ('message', _type),
        ])),
    ])
    data = '8\x07'
    msg = protolite.decode(proto, data)
    want = dict([('type', 'msg-type')])
    equal(want, msg)


def test_encode_enum_simple():
    # Don't check against data string since protolite doesn't use OrderedDict
    enc_type = dict([
        ('msg-type', 7),
    ])
    enc_proto = dict([
        ('type', dict([
            ('type', 'enum'),
            ('field', 7),
            ('message', enc_type),
        ])),
    ])
    dec_type = dict([
        (7, 'msg-type'),
    ])
    dec_proto = dict([
        (7, dict([
            ('type', 'enum'),
            ('name', 'type'),
            ('message', dec_type),
        ])),
    ])
    msg = dict([('type', 'msg-type')])
    data = protolite.encode(enc_proto, msg)
    res = protolite.decode(dec_proto, data)
    equal(msg, res)
