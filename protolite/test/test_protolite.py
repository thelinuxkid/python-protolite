from nose.tools import eq_ as equal

from protolite import protolite


class decoding(object):
    message_foo = dict([
        (1, dict([
            ('type', 'string'),
            ('name', 'body'),
        ])),
    ])
    message_bar = dict([
        (1, dict([
            ('type', 'enum'),
            ('name', 'type'),
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
    message_sna = dict([
        (1, dict([
            ('type', 'enum'),
            ('name', 'type'),
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
    message_bar = dict([
        ('type', dict([
            ('type', 'enum'),
            ('field', 1),
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
    message_sna = dict([
        ('type', dict([
            ('type', 'enum'),
            ('field', 1),
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


def test_decode_delimited_varint():
    dec_message = dict([
        (1, dict([
            ('type', 'string'),
            ('name', 'first_name'),
        ])),
    ])
    dec_proto = dict([
        (305, dict([
            ('type', 'embedded'),
            ('name', 'dec_message'),
            ('message', dec_message),
        ])),
    ])
    data = '\x8a\x13\xcf\t'
    msg = protolite.decode(dec_proto, data)
    want = dict([
        ('dec_message', dict()),
    ])
    equal(want, msg)


def test_encode_delimited_varint():
    # Don't check against data string since protolite doesn't use OrderedDict
    def _index():
        for i in range(0, 22):
            for j in range(32, 127):
                yield j+(127*i), chr(j)*(i+1)
    enc_message = dict()
    for i, c in _index():
        enc_message[c] = dict([
            ('type', 'string'),
            ('field', i),
        ])
    enc_proto = dict([
        ('message_foo', dict([
            ('type', 'embedded'),
            ('field', 305),
            ('message', enc_message),
        ])),
    ])
    dec_message = dict()
    for i, c in _index():
        dec_message[i] = dict([
            ('type', 'string'),
            ('name', c),
        ])
    dec_proto = dict([
        (305, dict([
            ('type', 'embedded'),
            ('name', 'message_foo'),
            ('message', dec_message),
        ])),
    ])
    msg = dict()
    for i, c in _index():
        msg[c] = str(i)
    msg = dict([
        ('message_foo', msg),
    ])
    data = protolite.encode(enc_proto, msg)
    res = protolite.decode(dec_proto, data)
    equal(msg, res)


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
                ('type', 4),
            ])),
        ])),
        ('type', 8),
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
                ('type', 4),
            ])),
        ])),
        ('type', 8),
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
    proto = dict([
        (7, dict([
            ('type', 'enum'),
            ('name', 'type'),
        ])),
    ])
    data = '8\x07'
    msg = protolite.decode(proto, data)
    want = dict([('type', 7)])
    equal(want, msg)


def test_encode_enum_simple():
    # Don't check against data string since protolite doesn't use OrderedDict
    enc_proto = dict([
        ('type', dict([
            ('type', 'enum'),
            ('field', 7),
        ])),
    ])
    dec_proto = dict([
        (7, dict([
            ('type', 'enum'),
            ('name', 'type'),
        ])),
    ])
    msg = dict([('type', 7)])
    data = protolite.encode(enc_proto, msg)
    res = protolite.decode(dec_proto, data)
    equal(msg, res)

def test_decode_varint_key():
    dec_message = dict([
        (1, dict([
            ('type', 'string'),
            ('name', 'first_name'),
        ])),
    ])
    dec_proto = dict([
        (1, dict([
            ('type', 'enum'),
            ('name', 'type'),
        ])),
        (305, dict([
            ('type', 'embedded'),
            ('name', 'dec_message'),
            ('message', dec_message),
        ])),
    ])
    data = '\x08\xb1\x02\x8a\x13\xcf\t'
    msg = protolite.decode(dec_proto, data)
    want = dict([
        ('type', 305),
        ('dec_message', dict()),
    ])
    equal(want, msg)


def test_encode_varint_key():
    # Don't check against data string since protolite doesn't use OrderedDict
    enc_message = dict([
        ('first_name', dict([
            ('type', 'string'),
            ('field', 1),
        ])),
    ])
    enc_proto = dict([
        ('type', dict([
            ('type', 'enum'),
            ('field', 1),
        ])),
        ('message_foo', dict([
            ('type', 'embedded'),
            ('field', 305),
            ('message', enc_message),
        ])),
    ])
    dec_message = dict([
        (1, dict([
            ('type', 'string'),
            ('name', 'first_name'),
        ])),
    ])
    dec_proto = dict([
        (1, dict([
            ('type', 'enum'),
            ('name', 'type'),
        ])),
        (305, dict([
            ('type', 'embedded'),
            ('name', 'message_foo'),
            ('message', dec_message),
        ])),
    ])
    msg = dict([
        ('type', 305),
        ('message_foo', dict()),
    ])
    data = protolite.encode(enc_proto, msg)
    res = protolite.decode(dec_proto, data)
    equal(msg, res)
