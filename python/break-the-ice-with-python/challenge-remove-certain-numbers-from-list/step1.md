# Remove Certain Numbers from List

By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

## Example

If you are given the following list:

```bash
[12, 24, 35, 70, 88, 120, 155]
```

Then, the output of the program should be:

```bash
[24, 70, 120]
```

## Hints

- Use list comprehension to delete a bunch of element from a list.
- Use `enumerate()` to get `(index, value)` tuple.
