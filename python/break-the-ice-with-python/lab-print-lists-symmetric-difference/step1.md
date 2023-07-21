# Print Lists Symmetric Difference

Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/print_lists_symmetric_difference.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def print_lists_symmetric_difference():
    n = int(input())
    set1 = set(map(int, input().split()))

    m = int(input())
    set2 = set(map(int, input().split()))

    ans = list(set1 ^ set2)
    ans = sorted(ans)
    for i in ans:
        print(i)


print_lists_symmetric_difference()

```

This Python code defines a function called `print_lists_symmetric_difference`. Within the function, the user is prompted to enter two sets of integers.

The first input `n` is used to determine the number of integers in the first set. The `input` function is used to read a line of input from the user, which is then split into a list of integers using the `split` method and the `map` function. The resulting list is then converted to a set using the `set` function and assigned to the variable `set1`.

The second input `m` is used to determine the number of integers in the second set. The `input` function is used to read a line of input from the user, which is then split into a list of integers using the `split` method and the `map` function. The resulting list is then converted to a set using the `set` function and assigned to the variable `set2`.

The symmetric difference of the two sets is then calculated using the `^` operator, which returns a new set containing the elements that are in either of the sets, but not in both.

The resulting set is then converted to a list using the `list` function and assigned to the variable `ans`.

The `sorted` function is then used to sort the elements of the `ans` list in ascending order.

Finally, a `for` loop is used to iterate over the elements of the `ans` list, and each element is printed to the console using the `print` function.

Overall, this code demonstrates how to use sets and list manipulation in Python to calculate and print the symmetric difference of two sets of integers.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/print_lists_symmetric_difference.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

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

At this point, your code is running successfully!
