# Anagrams

## Problem

Given an array of strings, write a function to sort the array so that all anagrams are next to each other. An anagram is defined as a word or phrase formed by rearranging the letters of another word or phrase. For example, "act" and "cat" are anagrams of each other.

## Requirements

To solve this problem, the following requirements must be met:

- The function must group all anagrams together in the sorted array.
- There are no other sorting requirements other than the grouping of anagrams.
- The inputs may not be valid, so the function must handle invalid inputs.
- The function must fit in memory.

## Example Usage

The function should behave as follows in these scenarios:

- None -> Exception
- [] -> []
- General case
  - Input: ['ram', 'act', 'arm', 'bat', 'cat', 'tab']
  - Result: ['arm', 'ram', 'act', 'cat', 'bat', 'tab']
