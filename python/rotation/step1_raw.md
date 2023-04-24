# Rotation

Problem: Determine if a string s1 is a rotation of another string s2, by calling (only once) a function is_substring.

## Requirements

- Can we assume the string is ASCII?
  - Yes
  - Note: Unicode strings could require special handling depending on your language
- Is this case sensitive?
  - Yes
- Can we use additional data structures?
  - Yes
- Can we assume this fits in memory?
  - Yes

## Example Usage

- Any strings that differ in size -> False
- None, 'foo' -> False (any None results in False)
- ' ', 'foo' -> False
- ' ', ' ' -> True
- 'foobarbaz', 'barbazfoo' -> True
