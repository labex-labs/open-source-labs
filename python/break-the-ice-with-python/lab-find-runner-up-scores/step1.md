# Find Runner up Scores

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/find_runner_up_scores.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def find_runner_up_scores():
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(arr))
    arr = sorted(arr)
    print(arr[-2])


find_runner_up_scores()

```

This Python code defines a function called `find_runner_up_scores`. The function prompts the user to enter an integer `n`, which represents the number of scores to be entered. The `input` function is used to read the user's input, and the `int` function is used to convert the input value to an integer.

The `map` function is then used to read the user's input for the scores, which are entered as a space-separated list of integers. The `map` function is used to convert each input value to an integer, and the resulting map object is converted to a list using the `list` function.

The `set` function is then used to remove any duplicate scores from the list, and the resulting list is sorted in ascending order using the `sorted` function.

Finally, the second highest score in the list is printed to the console using the `print` function. This is done by accessing the second-to-last element in the list using the index `-2`.

Overall, this code demonstrates how to use Python functions such as `input`, `map`, `set`, `sorted`, and `print` to find the second highest score from a list of scores entered by the user.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/find_runner_up_scores.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

If the following string is given as input to the program:

```bash
5
2 3 6 6 5
```

Then, the output of the program should be:

```bash
5
```

At this point, your code is running successfully!
