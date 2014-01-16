import pytest

from protolite import encoder


class decoding(object):
    message_foo = dict([
        (1, dict([
            ('type', 'string'),
            ('name', 'body'),
            ('scope', 'optional'),
        ])),
        (2, dict([
            ('type', 'string'),
            ('name', 'messages'),
            ('scope', 'repeated'),
        ])),
    ])
    message_bar = dict([
        (1, dict([
            ('type', 'enum'),
            ('name', 'type'),
            ('scope', 'optional'),
        ])),
        (4, dict([
            ('type', 'embedded'),
            ('name', 'message_foo'),
            ('message', message_foo),
            ('scope', 'optional'),
        ])),
    ])
    message_baz = dict([
        (1, dict([
            ('type', 'embedded'),
            ('name', 'message_bar'),
            ('message', message_bar),
            ('scope', 'optional'),
        ])),
        (3, dict([
            ('type', 'uint64'),
            ('name', 'baz_id'),
            ('scope', 'optional'),
        ])),
    ])
    message_sna = dict([
        (1, dict([
            ('type', 'enum'),
            ('name', 'type'),
            ('scope', 'optional'),
        ])),
        (8, dict([
            ('type', 'embedded'),
            ('name', 'message_baz'),
            ('message', message_baz),
            ('scope', 'optional'),
        ])),
    ])
    foo = dict([
        (1, dict([
            ('type', 'uint64'),
            ('name', 'foo_id'),
            ('scope', 'optional'),
        ])),
        (2, dict([
            ('type', 'bool'),
            ('name', 'is_foo'),
            ('scope', 'optional'),
        ])),
        (3, dict([
            ('type', 'uint32'),
            ('name', 'foo_count'),
            ('scope', 'optional'),
        ])),
        (305, dict([
            ('type', 'int32'),
            ('name', 'foo_value'),
            ('scope', 'optional'),
        ])),
    ])
    bar = dict([
        (1, dict([
            ('type', 'uint64'),
            ('name', 'bar_id'),
            ('scope', 'optional'),
        ])),
        (2, dict([
            ('type', 'float'),
            ('name', 'bar_value'),
            ('scope', 'optional'),
        ])),
        (3, dict([
            ('type', 'double'),
            ('name', 'bar_result'),
            ('scope', 'optional'),
        ])),
        (5, dict([
            ('type', 'embedded'),
            ('name', 'foos'),
            ('message', foo),
            ('scope', 'repeated'),
        ])),
    ])
    sna = dict([
        (1, dict([
            ('type', 'uint64'),
            ('name', 'sna_ids'),
            ('scope', 'repeated'),
        ])),
        (2, dict([
            ('type', 'double'),
            ('name', 'snas'),
            ('scope', 'repeated'),
        ])),
        (3, dict([
            ('type', 'float'),
            ('name', 'foos'),
            ('scope', 'repeated'),
        ])),
        (4, dict([
            ('type', 'uint32'),
            ('name', 'counts'),
            ('scope', 'repeated'),
        ])),
    ])


class encoding(object):
    message_foo = dict([
        ('body', dict([
            ('type', 'string'),
            ('field', 1),
            ('scope', 'optional'),
        ])),
        ('messages', dict([
            ('type', 'string'),
            ('field', 2),
            ('scope', 'repeated'),
        ])),
    ])
    message_bar = dict([
        ('type', dict([
            ('type', 'enum'),
            ('field', 1),
            ('scope', 'optional'),
        ])),
        ('message_foo', dict([
            ('type', 'embedded'),
            ('field', 4),
            ('message', message_foo),
            ('scope', 'optional'),
        ])),
    ])
    message_baz = dict([
        ('message_bar', dict([
            ('type', 'embedded'),
            ('field', 1),
            ('message', message_bar),
            ('scope', 'optional'),
        ])),
        ('baz_id', dict([
            ('type', 'uint64'),
            ('field', 3),
            ('scope', 'optional'),
        ])),
    ])
    foo = dict([
        ('foo_id', dict([
            ('type', 'uint64'),
            ('field', 1),
            ('scope', 'optional'),
        ])),
        ('is_foo', dict([
            ('type', 'bool'),
            ('field', 2),
            ('scope', 'optional'),
        ])),
        ('foo_count', dict([
            ('type', 'uint32'),
            ('field', 3),
            ('scope', 'optional'),
        ])),
        ('foo_value', dict([
            ('type', 'int32'),
            ('field', 305),
            ('scope', 'optional'),
        ])),
    ])
    bar = dict([
        ('bar_id', dict([
            ('type', 'uint64'),
            ('field', 1),
            ('scope', 'optional'),
        ])),
        ('bar_value', dict([
            ('type', 'float'),
            ('field', 2),
            ('scope', 'optional'),
        ])),
        ('bar_result', dict([
            ('type', 'double'),
            ('field', 3),
            ('scope', 'optional'),
        ])),
        ('foos', dict([
            ('type', 'embedded'),
            ('field', 5),
            ('message', foo),
            ('scope', 'repeated'),
        ])),
    ])
    message_sna = dict([
        ('type', dict([
            ('type', 'enum'),
            ('field', 1),
            ('scope', 'optional'),
        ])),
        ('message_baz', dict([
            ('type', 'embedded'),
            ('field', 8),
            ('message', message_baz),
            ('scope', 'optional'),
        ])),
    ])
    sna = dict([
        ('sna_ids', dict([
            ('type', 'uint64'),
            ('field', 1),
            ('scope', 'repeated'),
        ])),
        ('snas', dict([
            ('type', 'double'),
            ('field', 2),
            ('scope', 'repeated'),
        ])),
        ('foos', dict([
            ('type', 'float'),
            ('field', 3),
            ('scope', 'repeated'),
        ])),
        ('counts', dict([
            ('type', 'uint32'),
            ('field', 4),
            ('scope', 'repeated'),
        ])),
    ])


def test_decode_key_as_varint():
    data = '\x88\x13\x08'
    msg = encoder.decode(decoding.foo, data)
    want = dict([
        ('foo_value', 8),
    ])
    assert want == msg


def test_encode_key_as_varint():
    # Don't check against data string since protolite doesn't use OrderedDict
    msg = dict([
        ('foo_value', 8),
    ])
    data = encoder.encode(encoding.foo, msg)
    res = encoder.decode(decoding.foo, data)
    assert msg == res


def test_decode_int32():
    data = '\x18\x7f'
    msg = encoder.decode(decoding.foo, data)
    want = dict([('foo_count', 127)])
    assert want == msg


def test_encode_int32():
    # Don't check against data string since protolite doesn't use OrderedDict
    msg = dict([('foo_count', 127)])
    data = encoder.encode(encoding.foo, msg)
    res = encoder.decode(decoding.foo, data)
    assert msg == res


def test_decode_uint64():
    data = '\x08\x80\xa0\x88\x84\x80\x8a\xa5\xfe\r'
    msg = encoder.decode(decoding.bar, data)
    want = dict([
        ('bar_id', 1007843487950966784L),
    ])
    assert want == msg


def test_encode_uint64():
    # Don't check against data string since encoder doesn't use OrderedDict
    msg = dict([
        ('bar_id', 1007843487950966784L),
    ])
    data = encoder.encode(encoding.bar, msg)
    res = encoder.decode(decoding.bar, data)
    assert msg == res


def test_encode_uint64_negative():
    with pytest.raises(ValueError) as einfo:
        msg = dict([
            ('bar_id', -155496620801056360),
        ])
        encoder.encode(encoding.bar, msg)
    want = 'ValueError: uint64 value cannot be negative: -155496620801056360'
    assert einfo.exconly() == want


def test_decode_bool():
    data = '\x10\x00'
    msg = encoder.decode(decoding.foo, data)
    want = dict([('is_foo', False)])
    assert want == msg


def test_encode_bool():
    # Don't check against data string since encoder doesn't use OrderedDict
    msg = dict([('is_foo', False)])
    data = encoder.encode(encoding.foo, msg)
    res = encoder.decode(decoding.foo, data)
    assert msg == res


def test_decode_enum():
    data = '\x08\x07'
    msg = encoder.decode(decoding.message_bar, data)
    want = dict([('type', 7)])
    assert want == msg


def test_encode_enum():
    # Don't check against data string since encoder doesn't use OrderedDict
    msg = dict([('type', 7)])
    data = encoder.encode(encoding.message_bar, msg)
    res = encoder.decode(decoding.message_bar, data)
    assert msg == res


def test_decode_repeated_varint():
    data = '\x08\n\x08\x14'
    msg = encoder.decode(decoding.sna, data)
    want = dict([
        ('sna_ids', [10, 20]),
    ])
    assert want == msg


def test_encode_repeated_varint():
    # Don't check against data string since encoder doesn't use OrderedDict
    msg = dict([
        ('sna_ids', [10, 20]),
    ])
    data = encoder.encode(encoding.sna, msg)
    res = encoder.decode(decoding.sna, data)
    assert msg == res


def test_encode_repeated_uint_negative():
    with pytest.raises(ValueError) as einfo:
        msg = dict([
            ('counts', [1, -2, 3]),
        ])
        encoder.encode(encoding.sna, msg)
    want = 'ValueError: uint32 value cannot be negative: -2'
    assert einfo.exconly() == want


def test_decode_64bit():
    data = '\x19\x00\x00\x00\xe0%\x99^\xc0'
    msg = encoder.decode(decoding.bar, data)
    want = dict([
        ('bar_result', -122.39293670654297),
    ])
    assert want == msg


def test_encode_64bit():
    # Don't check against data string since encoder doesn't use OrderedDict
    msg = dict([
        ('bar_result', -122.39293670654297),
    ])
    data = encoder.encode(encoding.bar, msg)
    res = encoder.decode(decoding.bar, data)
    assert msg == res


def test_decode_64bit_repeated():
    data = '\x11\x00\x00\x00\xe0%\x99^\xc0\x11\x8fB\x9a\xf4\xdcZm@'
    msg = encoder.decode(decoding.sna, data)
    want = dict([
        ('snas', [-122.39293670654297, 234.839472104348218943324]),
    ])
    assert want == msg


def test_encode_64bit_repeated():
    # Don't check against data string since encoder doesn't use OrderedDict
    msg = dict([
        ('snas', [-122.39293670654297, 234.839472104348218943324]),
    ])
    data = encoder.encode(encoding.sna, msg)
    res = encoder.decode(decoding.sna, data)
    assert msg == res


def test_decode_delimited_length_as_varint():
    dec_message = dict([
        (1, dict([
            ('type', 'string'),
            ('name', 'first_name'),
            ('scope', 'optional'),
        ])),
    ])
    dec_proto = dict([
        (305, dict([
            ('type', 'embedded'),
            ('name', 'dec_message'),
            ('message', dec_message),
            ('scope', 'optional'),
        ])),
    ])
    data = '\x8a\x13\xcf\t'
    msg = encoder.decode(dec_proto, data)
    # we don't care about the items, only the value of the length
    want = dict([
        ('dec_message', dict()),
    ])
    assert want == msg


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
            ('scope', 'optional'),
        ])
    enc_proto = dict([
        ('message_foo', dict([
            ('type', 'embedded'),
            ('field', 305),
            ('message', enc_message),
            ('scope', 'optional'),
        ])),
    ])
    dec_message = dict()
    for i, c in _index():
        dec_message[i] = dict([
            ('type', 'string'),
            ('name', c),
            ('scope', 'optional'),
        ])
    dec_proto = dict([
        (305, dict([
            ('type', 'embedded'),
            ('name', 'message_foo'),
            ('message', dec_message),
            ('scope', 'optional'),
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
    assert msg == res


def test_decode_embedded():
    data = '\x08\x08B\x12\n\r\x08\x04"\t\n\x07foobody\x18\xb9`'
    msg = encoder.decode(decoding.message_sna, data)
    want = dict([
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
    assert want == msg


def test_encode_embedded():
    # Don't check against data string since encoder doesn't use OrderedDict
    msg = dict([
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
    assert msg == res


def test_decode_string():
    data = '\n\hello world'
    msg = encoder.decode(decoding.message_foo, data)
    want = dict([
        ('body', 'hello world'),
    ])
    assert want == msg


def test_encode_string():
    # Don't check against data string since protolite doesn't use OrderedDict
    msg = dict([
        ('body', 'hello world'),
    ])
    data = encoder.encode(encoding.message_foo, msg)
    res = encoder.decode(decoding.message_foo, data)
    assert msg == res

    msg = dict([
        ('body', u'\u03b3\u03b5\u03b9\u03b1'),
    ])
    data = encoder.encode(encoding.message_foo, msg)
    res = encoder.decode(decoding.message_foo, data)
    assert msg == res


def test_decode_embedded_repeated():
    data = '\x08\x1e*\x02\x08\n*\x02\x08\x14'
    msg = encoder.decode(decoding.bar, data)
    want = dict([
        ('bar_id', 30),
        ('foos', [
            dict([('foo_id', 10)]),
            dict([('foo_id', 20)]),
        ]),
    ])
    assert want == msg


def test_encode_embedded_repeated():
    # Don't check against data string since encoder doesn't use OrderedDict
    msg = dict([
        ('bar_id', 30),
        ('foos', [
            dict([('foo_id', 10)]),
            dict([('foo_id', 20)]),
        ]),
    ])
    data = encoder.encode(encoding.bar, msg)
    res = encoder.decode(decoding.bar, data)
    assert msg == res


def test_decode_string_repeated():
    data = '\x12\x03bar\x12\x03baz'
    msg = encoder.decode(decoding.message_foo, data)
    want = dict([
        ('messages', ['bar', 'baz']),
    ])
    assert want == msg


def test_encode_string_repeated():
    # Don't check against data string since encoder doesn't use OrderedDict
    msg = dict([
        ('messages', ['bar', 'baz']),
    ])
    data = encoder.encode(encoding.message_foo, msg)
    res = encoder.decode(decoding.message_foo, data)
    assert msg == res


def test_decode_32bit():
    data = '\x15/\xc9\xf4\xc2'
    msg = encoder.decode(decoding.bar, data)
    want = dict([
        ('bar_value', -122.39293670654297),
    ])
    assert want == msg


def test_encode_32bit():
    # Don't check against data string since encoder doesn't use OrderedDict
    msg = dict([
        ('bar_value', -122.39293670654297),
    ])
    data = encoder.encode(encoding.bar, msg)
    res = encoder.decode(decoding.bar, data)
    assert msg == res


def test_decode_32bit_repeated():
    data = '\x1d/\xc9\xf4\xc2\x1d\xeb\xe2V?'
    msg = encoder.decode(decoding.sna, data)
    want = dict([
        ('foos', [-122.39293670654297, 0.8393999934196472]),
    ])
    assert want == msg


def test_encode_32bit_repeated():
    # Don't check against data string since encoder doesn't use OrderedDict
    msg = dict([
        ('foos', [-122.39293670654297, 0.8393999934196472]),
    ])
    data = encoder.encode(encoding.sna, msg)
    res = encoder.decode(decoding.sna, data)
    assert msg == res
