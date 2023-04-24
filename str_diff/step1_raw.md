# Str Diff

Problem: Find the single different char between two strings.

## Requirements

- Can we assume the strings are ASCII?
  - Yes
- Is case important?
  - The strings are lower case
- Can we assume the inputs are valid?
  - No, check for None
  - Otherwise, assume there is only a single different char between the two strings
- Can we assume this fits memory?
  - Yes

## Example Usage

- None input -> TypeError
- 'ab', 'aab' -> 'a'
- 'aab', 'ab' -> 'a'
- 'abcd', 'abcde' -> 'e'
- 'aaabbcdd', 'abdbacade' -> 'e'
