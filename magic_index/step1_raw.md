# Magic Index

Problem: Find the magic index in an array, where array[i] = i.

## Requirements

- Is the array sorted?
  - Yes
- Are the elements in the array distinct?
  - No
- Does a magic index always exist?
  - No
- If there is no magic index, do we just return -1?
  - Yes
- Are negative values allowed in the array?
  - Yes
- If there are multiple magic values, what do we return?
  - Return the left-most one
- Can we assume this fits memory?
  - Yes

## Example Usage

- None input -> -1
- Empty array -> -1

```txt
a[i]  -4 -2  2  6  6  6  6 10
  i    0  1  2  3  4  5  6  7
```

Result: 2

```txt
a[i]  -4 -2  1  6  6  6  6 10
  i    0  1  2  3  4  5  6  7
```

Result: 6

```txt
a[i]  -4 -2  1  6  6  6  7 10
  i    0  1  2  3  4  5  6  7
```

Result: -1
