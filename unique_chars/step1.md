# Unique Chars

## Problem

Given a string, the task is to determine if it contains all unique characters. In other words, there should be no repeated characters in the string. For example, the string "hello" does not have all unique characters because the letter "l" appears twice. On the other hand, the string "world" has all unique characters because each letter appears only once.

## Requirements

To solve this problem, the following requirements must be met:

- The string is assumed to be ASCII.
  - Unicode strings may require special handling depending on the language used.
- The case is assumed to be sensitive.
- Additional data structures can be used.
- It is assumed that the string fits in memory.

## Example Usage

The following are examples of how the function should behave:

- None -> False
- '' -> True
- 'foo' -> False
- 'bar' -> True
