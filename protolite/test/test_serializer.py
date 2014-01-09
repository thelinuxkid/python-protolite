from protolite import serializer


def test_decode_key_simple():
    field, wire = serializer.decode_key(8)
    assert 1 == field
    assert 0 == wire


def test_encode_key_simple():
    key = serializer.encode_key(1, 0)
    assert 8 == key


def test_decode_varint_simple():
    value, index = serializer.decode_varint([168, 172, 2], 0)
    assert 38440 == value
    assert 3 == index


def test_encode_varint_simple():
    value = serializer.encode_varint(38440)
    assert [168, 172, 2] == value


def test_decode_varint_uint64():
    data = [128, 160, 136, 132, 128, 138, 165, 254, 13]
    value, index = serializer.decode_varint(data, 0)
    assert 1007843487950966784L == value
    assert 9 == index


def test_encode_varint_uint64():
    value = serializer.encode_varint(1007843487950966784L)
    assert [128, 160, 136, 132, 128, 138, 165, 254, 13] == value


def test_decode_32bit_simple():
    value, index = serializer.decode_struct(
        [47, 201, 244, 194],
        0,
        4,
        '<f',
    )
    assert -122.39293670654297 == value
    assert 4 == index


def test_encode_32bit_simple():
    value = serializer.encode_struct(-122.39293670654297, '<f')
    assert [47, 201, 244, 194] == value


def test_decode_64bit_simple():
    value, index = serializer.decode_struct(
        [0, 0, 0, 224, 37, 153, 94, 192],
        0,
        8,
        '<d',
    )
    assert -122.39293670654297 == value
    assert 8 == index


def test_encode_64bit_simple():
    value = serializer.encode_struct(-122.39293670654297, '<d')
    assert [0, 0, 0, 224, 37, 153, 94, 192] == value


def test_decode_delimited_simple():
    data = [7, 116, 101, 115, 116, 105, 110, 103]
    value, index = serializer.decode_delimited(data, 0)
    assert [116, 101, 115, 116, 105, 110, 103] == value
    assert 8 == index


def test_encode_delimited_simple():
    value = serializer.encode_delimited('testing')
    want = [7, 116, 101, 115, 116, 105, 110, 103]
    assert want == value
