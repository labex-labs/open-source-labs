# N Pairs Parentheses

## Problem

The problem is to find all valid combinations of n-pairs of parentheses. A valid combination is one in which each opening parenthesis has a corresponding closing parenthesis and the pairs of parentheses are properly nested. For example, the following are valid combinations of 3-pairs of parentheses:

- ((()))
- (()())
- (())()
- ()(())
- ()()()

The following are not valid combinations of 3-pairs of parentheses:

- )()(
- ((()
- ))((
- ()()()

## Requirements

To solve this problem, we need to answer the following questions:

- Is the input an integer representing the number of pairs?
  - Yes, the input is an integer representing the number of pairs.
- Can we assume the inputs are valid?
  - No, we cannot assume the inputs are valid.
- Is the output a list of valid combinations?
  - Yes, the output is a list of valid combinations.
- Should the output have duplicates?
  - No, the output should not have duplicates.
- Can we assume this fits memory?
  - Yes, we can assume this fits memory.

## Example Usage

The following are example usages of the function:

- None -> Exception
- Negative -> Exception
- 0 -> []
- 1 -> ['()']
- 2 -> ['(())', '()()']
- 3 -> ['((()))', '(()())', '(())()', '()(())', '()()()']
