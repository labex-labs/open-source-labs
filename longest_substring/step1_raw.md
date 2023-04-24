# Longest Substring

Problem: Given two strings, find the longest common substring.

## Requirements

- Can we assume the inputs are valid?
  - No
- Can we assume the strings are ASCII?
  - Yes
- Is this case sensitive?
  - Yes
- Is a substring a contiguous block of chars?
  - Yes
- Do we expect a string as a result?
  - Yes
- Can we assume this fits memory?
  - Yes

## Example Usage

- str0 or str1 is None -> Exception
- str0 or str1 equals 0 -> ''
- General case

str0 = 'ABCDEFGHIJ'
str1 = 'FOOBCDBCDE'

result: 'BCDE'
