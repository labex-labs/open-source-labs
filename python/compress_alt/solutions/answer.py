def compress_string(string):
    if string is None or len(string) == 0:
        return string

    # Calculate the size of the compressed string
    size = 0
    last_char = string[0]
    for char in string:
        if char != last_char:
            size += 2
            last_char = char
    size += 2

    # If the compressed string size is greater than
    # or equal to string size, return original string
    if size >= len(string):
        return string

    # Create compressed_string
    # New objective:
    # Single characters are to be left as is
    # Double characters are to be left as are
    compressed_string = list()
    count = 0
    last_char = string[0]
    for char in string:
        if char == last_char:
            count += 1
        else:
            # Do the old compression tricks only if count exceeds two
            if count > 2:
                compressed_string.append(last_char)
                compressed_string.append(str(count))
                count = 1
                last_char = char
            # If count is either 1 or 2
            else:
                # If count is 1, leave the char as is
                if count == 1:
                    compressed_string.append(last_char)
                    count = 1
                    last_char = char
                # If count is 2, append the character twice
                else:
                    compressed_string.append(last_char)
                    compressed_string.append(last_char)
                    count = 1
                    last_char = char
    compressed_string.append(last_char)
    compressed_string.append(str(count))

    # Convert the characters in the list to a string
    return "".join(compressed_string)
def split_to_blocks(string):
    block = ''
    for char, next_char in zip(string, string[1:] + ' '):
        block += char
        if char is not next_char:
            yield block
            block = ''


def compress_block(block):
    if len(block) <= 2:
        return block
    else:
        return block[0] + str(len(block))


def compress_string(string):
    if string is None or not string:
        return string
    compressed = (compress_block(block) for block in split_to_blocks(string))
    result = ''.join(compressed)
    return result if len(result) < len(string) else string
