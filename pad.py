def left_pad_with_zeros(input_string, total_length):
    return input_string.zfill(total_length)


def right_pad_with_zeros(input_string, total_length):
    return input_string.ljust(total_length, '0')