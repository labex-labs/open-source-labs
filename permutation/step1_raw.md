# Permutation

Problem: Determine if a string is a permutation of another string.

## Requirements

- Can we assume the string is ASCII?
  - Yes
  - Note: Unicode strings could require special handling depending on your language
- Is whitespace important?
  - Yes
- Is this case sensitive? 'Nib', 'bin' is not a match?
  - Yes
- Can we use additional data structures?
  - Yes
- Can we assume this fits in memory?
  - Yes

## Example Usage

- One or more None inputs -> False
- One or more empty strings -> False
- 'Nib', 'bin' -> False
- 'act', 'cat' -> True
- 'a ct', 'ca t' -> True
