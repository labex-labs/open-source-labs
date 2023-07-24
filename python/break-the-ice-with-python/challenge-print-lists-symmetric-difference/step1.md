# Print Lists Symmetric Difference

Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

## Example

The first line of input contains an integer, M.The second line contains M space-separated integers.The third line contains an integer, N.The fourth line contains N space-separated integers.

```bash
4
2 4 5 9
4
2 4 11 12
```

Then, output the symmetric difference integers in ascending order, one per line.

```bash
5
9
11
12
```

## Hints

- Use `^` to make symmetric difference operation.
- Use `sorted()` method to sort a list.
