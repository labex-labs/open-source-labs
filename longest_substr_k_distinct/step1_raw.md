# Longest Substr K Distinct

Problem: Find the length of the longest substring with at most k distinct characters.

## Requirements

- Can we assume the inputs are valid?
  - No
- Can we assume the strings are ASCII?
  - Yes
- Is this case sensitive?
  - Yes
- Is a substring a contiguous block of chars?
  - Yes
- Do we expect an int as a result?
  - Yes
- Can we assume this fits memory?
  - Yes

## Example Usage

- None -> TypeError
- '', k = 3 -> 0
- 'abcabcdefgghiij', k=3 -> 6
- 'abcabcdefgghighij', k=3 -> 7
