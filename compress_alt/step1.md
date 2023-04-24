# Compress Alt

## Problem

Given a string, compress it such that consecutive occurrences of the same character are replaced with that character followed by the number of occurrences. For example, the string 'AAABCCDDDD' would become 'A3BCCD4'. However, if the compressed string is not shorter than the original string, return the original string.

## Requirements

To solve this challenge, the following requirements must be met:

- The string is assumed to be ASCII.
- The compression is case sensitive.
- Additional data structures can be used.
- The string is assumed to fit in memory.

## Example Usage

The following are examples of how this function can be used:

- `compress(None)` returns `None`
- `compress('')` returns `''`
- `compress('AABBCC')` returns `'AABBCC'`
- `compress('AAABCCDDDD')` returns `'A3BCCD4'`
