# Print Keys of a Dictionary

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

## Example

Suppose the following input is supplied to the program:

```bash
range(1, 21)
```

Then, the output of the program should be:

```bash
dict_keys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
```

## Hints

- Use `dict[key]=value` pattern to put entry into a dictionary.
- Use `**` operator to get power of a number.
- Use `range()` for loops.
- Use `keys()` to iterate keys in the dictionary. Also we can use `item()` to get key/value pairs.
