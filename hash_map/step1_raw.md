# Hash Map

Problem: Implement a hash table with set, get, and remove methods.

## Requirements

- For simplicity, are the keys integers only?
  - Yes
- For collision resolution, can we use chaining?
  - Yes
- Do we have to worry about load factors?
  - No
- Do we have to validate inputs?
  - No
- Can we assume this fits memory?
  - Yes

## Example Usage

- `get` no matching key -> KeyError exception
- `get` matching key -> value
- `set` no matching key -> new key, value
- `set` matching key -> update value
- `remove` no matching key -> KeyError exception
- `remove` matching key -> remove key, value
