# Steps

Problem: You are running up n steps. If you can take a single, double, or triple step, how many possible ways are there to run up to the nth step?

## Requirements

- If n == 0, what should the result be?
  - Go with 1, but discuss different approaches
- Can we assume the inputs are valid?
  - No
- Can we assume this fits memory?
  - Yes

## Example Usage

- None or negative input -> Exception
- n == 0 -> 1
- n == 1 -> 1
- n == 2 -> 2
- n == 3 -> 4
- n == 4 -> 7
- n == 10 -> 274
