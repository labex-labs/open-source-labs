# Fizz Buzz

## Problem

Implement Fizz Buzz using Python. Your function should take an integer n as input and return a list of strings representing the numbers from 1 to n, with the following modifications:

- Multiples of 3 should be replaced with the string "Fizz"
- Multiples of 5 should be replaced with the string "Buzz"
- Multiples of both 3 and 5 should be replaced with the string "FizzBuzz"

Your function should also handle the following cases:

- If the input is less than 1, raise an exception
- If the input is not a valid integer, raise an exception

## Requirements

To implement Fizz Buzz in Python, we need to follow these requirements:

- Define a function that takes an integer n as input
- Check if the input is a valid integer and raise an exception if it is not
- Check if the input is less than 1 and raise an exception if it is
- Create a list of strings representing the numbers from 1 to n, with the modifications described above
- Return the list

## Example Usage

```python
assert fizz_buzz(15) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
```

```python
try:
    fizz_buzz(0)
except ValueError:
    print("Invalid input")
```

```python
try:
    fizz_buzz("hello")
except ValueError:
    print("Invalid input")
```

```python
try:
    fizz_buzz(-5)
except ValueError:
    print("Invalid input")
```
