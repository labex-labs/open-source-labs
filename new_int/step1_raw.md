# New Int

Problem: Given an array of 32 integers, find an int not in the input. Use a minimal amount of memory.

## Requirements

- Are we working with non-negative ints?
  - Yes
- What is the range of the integers?
  - Discuss the approach for 4 billion integers
  - Implement for 32 integers
- Can we assume the inputs are valid?
  - No

## Example Usage

- None -> Exception
- [] -> Exception
- General case
  - There is an int excluded from the input -> int
  - There isn't an int excluded from the input -> None
