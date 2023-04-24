This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# Solution Notebook

## Problem: Implement a trie with find, insert, remove, and list_words methods.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Can we assume we are working with strings?
  - Yes
- Are the strings in ASCII?
  - Yes
- Should `find` only match exact words with a terminating character?
  - Yes
- Should `list_words` only return words with a terminating character?
  - Yes
- Can we assume this fits memory?
  - Yes

## Test Cases

<pre>

root node is denoted by ''

         ''
       /  |  \
      h   a*  m
     / \   \   \
    a   e*  t*  e*
   / \         / \
  s*  t*      n*  t*
             /
            s*

find

* Find on an empty trie
* Find non-matching
* Find matching

insert

* Insert on empty trie
* Insert to make a leaf terminator char
* Insert to extend an existing terminator char

remove

* Remove me
* Remove mens
* Remove a
* Remove has

list_words

* List empty
* List general case
</pre>

## Algorithm

### find

- Set node to the root
- For each char in the input word
  - Check the current node's children to see if it contains the char
    - If a child has the char, set node to the child
    - Else, return None
- Return the last child node if it has a terminator, else None

Complexity:

- Time: O(m), where m is the length of the word
- Space: O(h) for the recursion depth (tree height), or O(1) if using an iterative approach

### insert

- set node to the root
- For each char in the input word
  - Check the current node's children to see if it contains the char
    - If a child has the char, set node to the child
    - Else, insert a new node with the char
      - Update children and parents
- Set the last node as a terminating node

Complexity:

- Time: O(m), where m is the length of the word
- Space: O(h) for the recursion depth (tree height), or O(1) if using an iterative approach

### remove

- Determine the matching terminating node by calling the find method
- If the matching node has children, remove the terminator to prevent orphaning its children
- Set the parent node to the matching node's parent
- We'll be looping up the parent chain to propagate the delete
- While the parent is valid
  - If the node has children
    - Return to prevent orphaning its remaining children
  - If the node is a terminating node and it isn't the original matching node from the find call
    - Return to prevent deleting this additional valid word
  - Remove the parent node's child entry matching the node
  - Set the node to the parent
  - Set the parent to the parent's parent

Complexity:

- Time: O(m+h), where where m is the length of the word and h is the tree height
- Space: O(h) for the recursion depth (tree height), or O(1) if using an iterative approach

### list_words

- Do a pre-order traversal, passing down the current word
  - When you reach a terminating node, add it to the list of results

Complexity:

- Time: O(n)
- Space: O(h) for the recursion depth (tree height), or O(1) if using an iterative approach

## Code

```python
%%writefile trie.py
from collections import OrderedDict


class Node(object):

    def __init__(self, key, parent=None, terminates=False):
        self.key = key
        self.terminates = False
        self.parent = parent
        self.children = {}


class Trie(object):

    def __init__(self):
        self.root = Node('')

    def find(self, word):
        if word is None:
            raise TypeError('word cannot be None')
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node if node.terminates else None

    def insert(self, word):
        if word is None:
            raise TypeError('word cannot be None')
        node = self.root
        parent = None
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = Node(char, parent=node)
                node = node.children[char]
        node.terminates = True

    def remove(self, word):
        if word is None:
            raise TypeError('word cannot be None')
        node = self.find(word)
        if node is None:
            raise KeyError('word does not exist')
        node.terminates = False
        parent = node.parent
        while parent is not None:
            # As we are propagating the delete up the
            # parents, if this node has children, stop
            # here to prevent orphaning its children.
            # Or
            # if this node is a terminating node that is
            # not the terminating node of the input word,
            # stop to prevent removing the associated word.
            if node.children or node.terminates:
                return
            del parent.children[node.key]
            node = parent
            parent = parent.parent

    def list_words(self):
        result = []
        curr_word = ''
        self._list_words(self.root, curr_word, result)
        return result

    def _list_words(self, node, curr_word, result):
        if node is None:
            return
        for key, child in node.children.items():
            if child.terminates:
                result.append(curr_word + key)
            self._list_words(child, curr_word + key, result)
```

    Overwriting trie.py

```python
%run trie.py
```

## Unit Test

```python
%%writefile test_trie.py
import unittest


class TestTrie(unittest.TestCase):

    def test_trie(self):
        trie = Trie()

        print('Test: Insert')
        words = ['a', 'at', 'has', 'hat', 'he',
                 'me', 'men', 'mens', 'met']
        for word in words:
            trie.insert(word)
        for word in trie.list_words():
            self.assertTrue(trie.find(word) is not None)

        print('Test: Remove me')
        trie.remove('me')
        words_removed = ['me']
        words = ['a', 'at', 'has', 'hat', 'he',
                 'men', 'mens', 'met']
        for word in words:
            self.assertTrue(trie.find(word) is not None)
        for word in words_removed:
            self.assertTrue(trie.find(word) is None)

        print('Test: Remove mens')
        trie.remove('mens')
        words_removed = ['me', 'mens']
        words = ['a', 'at', 'has', 'hat', 'he',
                 'men', 'met']
        for word in words:
            self.assertTrue(trie.find(word) is not None)
        for word in words_removed:
            self.assertTrue(trie.find(word) is None)

        print('Test: Remove a')
        trie.remove('a')
        words_removed = ['a', 'me', 'mens']
        words = ['at', 'has', 'hat', 'he',
                 'men', 'met']
        for word in words:
            self.assertTrue(trie.find(word) is not None)
        for word in words_removed:
            self.assertTrue(trie.find(word) is None)

        print('Test: Remove has')
        trie.remove('has')
        words_removed = ['a', 'has', 'me', 'mens']
        words = ['at', 'hat', 'he',
                 'men', 'met']
        for word in words:
            self.assertTrue(trie.find(word) is not None)
        for word in words_removed:
            self.assertTrue(trie.find(word) is None)

        print('Success: test_trie')

    def test_trie_remove_invalid(self):
        print('Test: Remove from empty trie')
        trie = Trie()
        self.assertTrue(trie.remove('foo') is None)


def main():
    test = TestTrie()
    test.test_trie()
    test.assertRaises(KeyError, test.test_trie_remove_invalid)


if __name__ == '__main__':
    main()
```

    Overwriting test_trie.py

```python
%run -i test_trie.py
```

    Test: Insert
    Test: Remove me
    Test: Remove mens
    Test: Remove a
    Test: Remove has
    Success: test_trie
    Test: Remove from empty trie
