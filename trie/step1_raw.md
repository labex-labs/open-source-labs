# Trie

Problem: Implement a trie with find, insert, remove, and list_words methods.

## Requirements

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

## Example Usage

<pre>

         root
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
