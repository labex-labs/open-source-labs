# Solution Notebook

This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Implement a hash table with set, get, and remove methods.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- For simplicity, are the keys integers only?
  - Yes
- For collision resolution, can we use chaining?
  - Yes
- Do we have to worry about load factors?
  - No
- Do we have to validate inputs?
  - No
- Can we assume this fits memory?
  - Yes

## Test Cases

- `get` no matching key -> KeyError exception
- `get` matching key -> value
- `set` no matching key -> new key, value
- `set` matching key -> update value
- `remove` no matching key -> KeyError exception
- `remove` matching key -> remove key, value

## Algorithm

### Hash Function

- Return key % table size

Complexity:

- Time: O(1)
- Space: O(1)

### Set

- Get hash index for lookup
- If key exists, replace
- Else, add

Complexity:

- Time: O(1) average and best, O(n) worst
- Space: O(1) space for newly added element

### Get

- Get hash index for lookup
- If key exists, return value
- Else, raise KeyError

Complexity:

- Time: O(1) average and best, O(n) worst
- Space: O(1)

### Remove

- Get hash index for lookup
- If key exists, delete the item
- Else, raise KeyError

Complexity:

- Time: O(1) average and best, O(n) worst
- Space: O(1)

## Code

```python
class Item(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return key % self.size

    def set(self, key, value):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_index].append(Item(key, value))

    def get(self, key):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
        raise KeyError('Key not found')

    def remove(self, key):
        hash_index = self._hash_function(key)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][index]
                return
        raise KeyError('Key not found')
```

## Unit Test

```python
%%writefile test_hash_map.py
import unittest


class TestHashMap(unittest.TestCase):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        hash_table = HashTable(10)

        print("Test: get on an empty hash table index")
        self.assertRaises(KeyError, hash_table.get, 0)

        print("Test: set on an empty hash table index")
        hash_table.set(0, 'foo')
        self.assertEqual(hash_table.get(0), 'foo')
        hash_table.set(1, 'bar')
        self.assertEqual(hash_table.get(1), 'bar')

        print("Test: set on a non empty hash table index")
        hash_table.set(10, 'foo2')
        self.assertEqual(hash_table.get(0), 'foo')
        self.assertEqual(hash_table.get(10), 'foo2')

        print("Test: set on a key that already exists")
        hash_table.set(10, 'foo3')
        self.assertEqual(hash_table.get(0), 'foo')
        self.assertEqual(hash_table.get(10), 'foo3')

        print("Test: remove on a key that already exists")
        hash_table.remove(10)
        self.assertEqual(hash_table.get(0), 'foo')
        self.assertRaises(KeyError, hash_table.get, 10)

        print("Test: remove on a key that doesn't exist")
        self.assertRaises(KeyError, hash_table.remove, -1)

        print('Success: test_end_to_end')


def main():
    test = TestHashMap()
    test.test_end_to_end()


if __name__ == '__main__':
    main()
```

    Overwriting test_hash_map.py

```python
run -i test_hash_map.py
```

    Test: get on an empty hash table index
    Test: set on an empty hash table index
    Test: set on a non empty hash table index
    Test: set on a key that already exists
    Test: remove on a key that already exists
    Test: remove on a key that doesn't exist
    Success: test_end_to_end

```python

```
