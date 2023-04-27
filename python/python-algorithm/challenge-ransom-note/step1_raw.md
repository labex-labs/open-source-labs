# Ransom Note

Problem: Given a magazine, see if a ransom note could have been written using the letters in the magazine.

## Requirements

- Is this case sensitive?
  - Yes
- Can we assume we're working with ASCII characters?
  - Yes
- Can we scan the entire magazine, or should we scan only when necessary?
  - You can scan the entire magazine
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Example Usage

- None -> Exception
- '', '' -> Exception
- 'a', 'b' -> False
- 'aa', 'ab' -> False
- 'aa', 'aab' -> True
