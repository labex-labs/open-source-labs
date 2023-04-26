# Hash Map

## Problem

Implement a hash table with set, get, and remove methods. The hash table should use chaining for collision resolution. The keys are integers only. We do not have to worry about load factors or validate inputs. We can assume that the hash table fits in memory.

## Requirements

- The keys are integers only.
- Chaining is used for collision resolution.
- Load factors do not need to be considered.
- Inputs do not need to be validated.
- The hash table fits in memory.

## Example Usage

- `get` method:
  - If there is no matching key, a KeyError exception is raised.
  - If there is a matching key, the corresponding value is returned.
- `set` method:
  - If there is no matching key, a new key-value pair is added to the hash table.
  - If there is a matching key, the corresponding value is updated.
- `remove` method:
  - If there is no matching key, a KeyError exception is raised.
  - If there is a matching key, the corresponding key-value pair is removed from the hash table.
