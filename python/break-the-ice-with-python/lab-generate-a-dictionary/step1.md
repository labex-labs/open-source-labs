# Generate a Dictionary

With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). And then the program should print the dictionary.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/generate_a_dictionary.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def generate_a_dictionary():
    n = int(input())
    ans = {i: i*i for i in range(1, n+1)}
    print(ans)


generate_a_dictionary()

```

This Python code defines a function called `generate_a_dictionary`. The function prompts the user to enter an integer `n`, which represents the number of key-value pairs to be entered into the dictionary. The `input` function is used to read the user's input, and the `int` function is used to convert the input value to an integer.

A dictionary is then created using a dictionary comprehension. The comprehension creates a key-value pair for each integer `i` in the range from 1 to `n`, where the key is `i` and the value is `i*i`.

Finally, the resulting dictionary is printed to the console using the `print` function.

Overall, this code demonstrates how to use a dictionary comprehension in Python to create a dictionary with a specific number of key-value pairs, where the values are calculated based on the keys.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/generate_a_dictionary.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
8
```

Then, the output of the program should be:

```bash
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
```

At this point, your code is running successfully!
