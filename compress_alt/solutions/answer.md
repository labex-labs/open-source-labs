This notebook was prepared by [hashhar](https://github.com/hashhar), second solution added by [janhak](https://github.com/janhak). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Compress a string such that 'AAABCCDDDD' becomes 'A3BCCD4'. Only compress the string if it saves space.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume the string is ASCII?
  - Yes
  - Note: Unicode strings could require special handling depending on your language
- Is this case sensitive?
  - Yes
- Can we use additional data structures?
  - Yes
- Can we assume this fits in memory?
  - Yes

## Test Cases

- None -> None
- '' -> ''
- 'AABBCC' -> 'AABBCC'
- 'AAABCCDDDD' -> 'A3BCCD4'

## Algorithm

Since Python strings are immutable, we'll use a list of characters to build the compressed string representation. We'll then convert the list to a string.

- Calculate the size of the compressed string
  - Note the constraint about compressing only if it saves space
- If the compressed string size is >= string size, return string
- Create compressed_string
  - For each char in string
    - If char is the same as last_char, increment count
    - Else
      - If the count is more than 2
        - Append last_char to compressed_string
        - append count to compressed_string
        - count = 1
        - last_char = char
      - If count is 1
        - Append last_char to compressed_string
        - count = 1
        - last_char = char
      - If count is 2
        - Append last_char to compressed_string
        - Append last_char to compressed_string once more
        - count = 1
        - last_char = char
    - Append last_char to compressed_string
    - Append count to compressed_string
  - Return compressed_string

Complexity:

- Time: O(n)
- Space: O(n)

## Code

```python
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
```

## Algorithm: Split to blocks and compress

Let us split the string first into blocks of identical characters and then compress it block by block.

- Split the string to blocks

  - For each character in string
    - Add this character to block
    - If the next character is different
      - Return block
      - Erase the content of block

- Compress block

  - If block consists of two or fewer characters
    - Return block
  - Else
    - Append length of the block to the first character and return

- Compress string
  - Split the string to blocks
  - Compress blocks
  - Join compressed blocks
  - Return result if it is shorter than original string

Complexity:

- Time: O(n)
- Space: O(n)

```python
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
```

## Unit Test

```python
%%writefile test_compress.py
import unittest


class TestCompress(unittest.TestCase):

    def test_compress(self, func):
        self.assertEqual(func(None), None)
        self.assertEqual(func(''), '')
        self.assertEqual(func('AABBCC'), 'AABBCC')
        self.assertEqual(func('AAABCCDDDD'), 'A3BCCD4')
        self.assertEqual(
            func('aaBCCEFFFFKKMMMMMMP taaammanlaarrrr seeeeeeeeek tooo'),
            'aaBCCEF4KKM6P ta3mmanlaar4 se9k to3',
        )
        print('Success: test_compress')


def main():
    test = TestCompress()
    test.test_compress(compress_string)


if __name__ == '__main__':
    main()
```

    Overwriting test_compress.py

```python
%run -i test_compress.py
```

    Success: test_compress
