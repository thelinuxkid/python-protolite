from nose.tools import eq_ as equal

from protolite import encoder


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
        (2, dict([
            ('type', 'bool'),
            ('name', 'is_foo'),
        ])),
        (3, dict([
            ('type', 'uint32'),
            ('name', 'foo_count'),
        ])),
        (305, dict([
            ('type', 'int32'),
            ('name', 'foo_value'),
        ])),
    ])
    bar = dict([
        (1, dict([
            ('type', 'uint64'),
            ('name', 'bar_id'),
        ])),
        (2, dict([
            ('type', 'float'),
            ('name', 'bar_value'),
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
        ('is_foo', dict([
            ('type', 'bool'),
            ('field', 2),
        ])),
        ('foo_count', dict([
            ('type', 'uint32'),
            ('field', 3),
        ])),
        ('foo_value', dict([
            ('type', 'int32'),
            ('field', 305),
        ])),
    ])
    bar = dict([
        ('bar_id', dict([
            ('type', 'uint64'),
            ('field', 1),
        ])),
        ('bar_value', dict([
            ('type', 'float'),
            ('field', 2),
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


def test_decode_key_as_varint():
    data = '\x88\x13\x08'
    msg = encoder.decode(decoding.foo, data)
    want = dict([
        ('foo_value', 8),
    ])
    equal(want, msg)

def test_encode_key_as_varint():
    # Don't check against data string since protolite doesn't use OrderedDict
    msg = dict([
        ('foo_value', 8),
    ])
    data = encoder.encode(encoding.foo, msg)
    res = encoder.decode(decoding.foo, data)
    equal(msg, res)


def test_decode_int32():
    data= '\x18\x7f'
    msg = encoder.decode(decoding.foo, data)
    want = dict([('foo_count', 127)])
    equal(want, msg)


def test_encode_int32():
    # Don't check against data string since protolite doesn't use OrderedDict
    msg = dict([('foo_count', 127)])
    data = encoder.encode(encoding.foo, msg)
    res = encoder.decode(decoding.foo, data)
    equal(msg, res)


def test_decode_uint64():
    data = '\x08\x80\xa0\x88\x84\x80\x8a\xa5\xfe\r'
    msg = encoder.decode(decoding.bar, data)
    want = dict([
        ('bar_id', 1007843487950966784L),
    ])
    equal(want, msg)


def test_encode_uint64():
    # Don't check against data string since encoder doesn't use OrderedDict
    msg = dict([
        ('bar_id', 1007843487950966784L),
    ])
    data = encoder.encode(encoding.bar, msg)
    res = encoder.decode(decoding.bar, data)
    equal(msg, res)


def test_decode_bool():
    data = '\x10\x00'
    msg = encoder.decode(decoding.foo, data)
    want = dict([('is_foo', False)])
    equal(want, msg)


def test_encode_bool():
    # Don't check against data string since encoder doesn't use OrderedDict
    msg = dict([('is_foo', False)])
    data = encoder.encode(encoding.foo, msg)
    res = encoder.decode(decoding.foo, data)
    equal(msg, res)


def test_decode_enum():
    data = '\x08\x07'
    msg = encoder.decode(decoding.message_bar, data)
    want = dict([('type', 7)])
    equal(want, msg)


def test_encode_enum():
    # Don't check against data string since encoder doesn't use OrderedDict
    msg = dict([('type', 7)])
    data = encoder.encode(encoding.message_bar, msg)
    res = encoder.decode(decoding.message_bar, data)
    equal(msg, res)


def test_decode_delimited_length_as_varint():
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
    msg = encoder.decode(dec_proto, data)
    # we don't care about the items, only the value of the length
    want = dict([
        ('dec_message', dict()),
    ])
    equal(want, msg)


def test_encode_delimited_length_as_varint():
    # Don't check against data string since encoder doesn't use OrderedDict
    # We need lots of items to create a large length value
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
    data = encoder.encode(enc_proto, msg)
    res = encoder.decode(dec_proto, data)
    equal(msg, res)


def test_decode_embedded():
    data = '\x08\x08B\x12\n\r\x08\x04"\t\n\x07foobody\x18\xb9`'
    msg = encoder.decode(decoding.message_sna, data)
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
    # Don't check against data string since encoder doesn't use OrderedDict
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
    data = encoder.encode(encoding.message_sna, msg)
    res = encoder.decode(decoding.message_sna, data)
    equal(msg, res)


def test_decode_string():
    data = '\n\hello world'
    msg = encoder.decode(decoding.message_foo, data)
    want = dict([
      ('body', 'hello world'),
    ])
    equal(want, msg)


def test_encode_string():
    # Don't check against data string since protolite doesn't use OrderedDict
    msg = dict([
      ('body', 'hello world'),
    ])
    data = encoder.encode(encoding.message_foo, msg)
    res = encoder.decode(decoding.message_foo, data)
    equal(msg, res)


def test_decode_repeated():
    data = '\x08\n*\x02\x08\n*\x02\x08\x14'
    msg = encoder.decode(decoding.bar, data)
    want = dict([
      ('bar_id', 10),
      ('foos', [
        dict([('foo_id', 10)]),
        dict([('foo_id', 20)]),
      ]),
    ])
    equal(want, msg)


def test_encode_repeated():
    # Don't check against data string since encoder doesn't use OrderedDict
    msg = dict([
      ('bar_id', 10),
      ('foos', [
        dict([('foo_id', 10)]),
        dict([('foo_id', 20)]),
      ]),
    ])
    data = encoder.encode(encoding.bar, msg)
    res = encoder.decode(decoding.bar, data)
    equal(msg, res)


def test_decode_float():
    data = '\x15/\xc9\xf4\xc2'
    msg = encoder.decode(decoding.bar, data)
    want = dict([
        ('bar_value', -122.39293670654297),
    ])
    equal(want, msg)


def test_encode_float():
    # Don't check against data string since encoder doesn't use OrderedDict
    msg = dict([
        ('bar_value', -122.39293670654297),
    ])
    data = encoder.encode(encoding.bar, msg)
    res = encoder.decode(decoding.bar, data)
    equal(msg, res)
