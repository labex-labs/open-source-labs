# Print Words in Order

Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/print_words_in_order.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def print_words_in_order():
    lst = input().split(',')
    lst.sort()
    print(",".join(lst))


print_words_in_order()

```

This code defines a function called `print_words_in_order`. Within the function, the `input` function is used to prompt the user to enter a comma-separated list of words. The resulting string is then split into a list of words using the `split` method and stored in the variable `lst`.

The `sort` method is then used to sort the list of words in alphabetical order.

Finally, the `print` function is used to print the sorted list of words as a comma-separated string using the `join` method. The `join` method concatenates the elements of a list into a single string, using the specified separator (in this case, a comma `,`) between each element.

The resulting output is a sorted list of words in alphabetical order, separated by commas.

Overall, this code demonstrates how to use the `split`, `sort`, and `join` methods in Python to manipulate a list of words entered by the user and print them in alphabetical order.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/print_words_in_order.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
without,hello,bag,world
```

Then, the output of the program should be:

```bash
bag,hello,without,world
```

At this point, your code is running successfully!
