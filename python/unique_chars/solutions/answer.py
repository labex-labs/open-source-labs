class UniqueCharsSet(object):
    def has_unique_chars(self, string):
        if string is None:
            return False
        return len(set(string)) == len(string)


class UniqueChars(object):
    def has_unique_chars(self, string):
        if string is None:
            return False
        chars_set = set()
        for char in string:
            if char in chars_set:
                return False
            else:
                chars_set.add(char)
        return True


class UniqueCharsInPlace(object):
    def has_unique_chars(self, string):
        if string is None:
            return False
        for char in string:
            if string.count(char) > 1:
                return False
        return True
