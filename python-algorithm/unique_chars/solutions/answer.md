This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Implement an algorithm to determine if a string has all unique characters.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm 1: Sets and Length Comparison](#Algorithm-1:-Sets-and-Length-Comparison)
- [Code: Sets and Length Comparison](#Code:-Sets-and-Length-Comparison)
- [Algorithm 2: Hash Map Lookup](#Algorithm-2:-Hash-Map-Lookup)
- [Code: Hash Map Lookup](#Code:-Hash-Map-Lookup)
- [Algorithm 3: In-Place](#Algorithm-3:-In-Place)
- [Code: In-Place](#Code:-In-Place)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume the string is ASCII?
  - Yes
  - Note: Unicode strings could require special handling depending on your language
- Can we assume this is case sensitive?
  - Yes
- Can we use additional data structures?
  - Yes
- Can we assume this fits in memory?
  - Yes

## Test Cases

- None -> False
- '' -> True
- 'foo' -> False
- 'bar' -> True

## Algorithm 1: Sets and Length Comparison

A set is an unordered collection of unique elements.

- If the length of the set(string) equals the length of the string
  - Return True
- Else
  - Return False

Complexity:

- Time: O(n)
- Space: Additional O(n)

## Code: Sets and Length Comparison

```python
class UniqueCharsSet(object):

    def has_unique_chars(self, string):
        if string is None:
            return False
        return len(set(string)) == len(string)
```

## Algorithm 2: Hash Map Lookup

We'll keep a hash map (set) to keep track of unique characters we encounter.

Steps:

- Scan each character
- For each character:
  - If the character does not exist in a hash map, add the character to a hash map
  - Else, return False
- Return True

Notes:

- We could also use a dictionary, but it seems more logical to use a set as it does not contain duplicate elements
- Since the characters are in ASCII, we could potentially use an array of size 128 (or 256 for extended ASCII)

Complexity:

- Time: O(n)
- Space: Additional O(n)

## Code: Hash Map Lookup

```python
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
```

## Algorithm 3: In-Place

Assume we cannot use additional data structures, which will eliminate the fast lookup O(1) time provided by our hash map.

- Scan each character
- For each character:
  - Scan all [other] characters in the array
    - Excluding the current character from the scan is rather tricky in Python and results in a non-Pythonic solution
    - If there is a match, return False
- Return True

Algorithm Complexity:

- Time: O(n^2)
- Space: O(1)

## Code: In-Place

```python
class UniqueCharsInPlace(object):

    def has_unique_chars(self, string):
        if string is None:
            return False
        for char in string:
            if string.count(char) > 1:
                return False
        return True
```

## Unit Test

```python
%%writefile test_unique_chars.py
import unittest


class TestUniqueChars(unittest.TestCase):

    def test_unique_chars(self, func):
        self.assertEqual(func(None), False)
        self.assertEqual(func(''), True)
        self.assertEqual(func('foo'), False)
        self.assertEqual(func('bar'), True)
        print('Success: test_unique_chars')


def main():
    test = TestUniqueChars()
    unique_chars = UniqueChars()
    test.test_unique_chars(unique_chars.has_unique_chars)
    try:
        unique_chars_set = UniqueCharsSet()
        test.test_unique_chars(unique_chars_set.has_unique_chars)
        unique_chars_in_place = UniqueCharsInPlace()
        test.test_unique_chars(unique_chars_in_place.has_unique_chars)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()
```

    Overwriting test_unique_chars.py

```python
%run -i test_unique_chars.py
```

    Success: test_unique_chars
    Success: test_unique_chars
    Success: test_unique_chars
