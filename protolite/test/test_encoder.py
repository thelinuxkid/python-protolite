from nose.tools import eq_ as equal

from protolite import encoder


def test_decode_key_simple():
    field, wire = encoder.decode_key(8)
    equal(1, field)
    equal(0, wire)


def test_encode_key_simple():
    key = encoder.encode_key(1,0)
    equal(8, key)


def test_decode_varint_simple():
    value, index = encoder.decode_varint([168, 172, 2], 0)
    equal(38440, value)
    equal(3, index)


def test_encode_varint_simple():
    value = encoder.encode_varint(38440)
    equal([168, 172, 2], value)


def test_decode_varint_uint64():
    data = [128, 160, 136, 132, 128, 138, 165, 254, 13]
    value, index = encoder.decode_varint(data, 0)
    equal(1007843487950966784L, value)
    equal(9, index)


def test_encode_varint_uint64():
    value = encoder.encode_varint(1007843487950966784L)
    equal([128, 160, 136, 132, 128, 138, 165, 254, 13], value)


def test_decode_32bit_simple():
    value, index = encoder.decode_struct(
        [47, 201, 244, 194],
        0,
        4,
        '<f',
    )
    equal(-122.39293670654297, value)
    equal(4, index)


def test_encode_32bit_simple():
    value = encoder.encode_struct(-122.39293670654297, '<f')
    equal([47, 201, 244, 194], value)


def test_decode_64bit_simple():
    value, index = encoder.decode_struct(
        [0, 0, 0, 224, 37, 153, 94, 192],
        0,
        8,
        '<d',
    )
    equal(-122.39293670654297, value)
    equal(8, index)


def test_encode_64bit_simple():
    value = encoder.encode_struct(-122.39293670654297, '<d')
    equal([0, 0, 0, 224, 37, 153, 94, 192], value)


def test_decode_delimited_simple():
    data = [7, 116, 101, 115, 116, 105, 110, 103]
    value, index = encoder.decode_delimited(data, 0)
    equal([116, 101, 115, 116, 105, 110, 103], value)
    equal(8, index)


def test_encode_delimited_simple():
    value = encoder.encode_delimited('testing')
    want = [7, 116, 101, 115, 116, 105, 110, 103]
    equal(want, value)
