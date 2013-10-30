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
