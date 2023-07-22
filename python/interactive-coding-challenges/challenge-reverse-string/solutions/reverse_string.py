class ReverseString(object):
    def reverse(self, chars):
        if chars:
            size = len(chars)
            for i in range(size // 2):
                chars[i], chars[size - 1 - i] = chars[size - 1 - i], chars[i]
        return chars


class ReverseStringAlt(object):
    def reverse_string_alt(string):
        if string:
            return string[::-1]
        return string

    def reverse_string_alt2(string):
        if string:
            return "".join(reversed(string))
        return string
