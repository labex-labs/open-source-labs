# Reverse Order String

Please write a program which accepts a string from console and print it in reverse order.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/reverse_order_string.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def reverse_order_string():
    s = input()
    s = ''.join(reversed(s))
    print(s)


reverse_order_string()

```

This Python code defines a function called `reverse_order_string()` that reverses the order of characters in a string. The function prompts the user to input a string using the `input()` function.

The function then uses the `reversed()` function to reverse the order of characters in the string. The `reversed()` function returns a reverse iterator that can be converted to a string using the `join()` method. The `join()` method concatenates the characters in the iterator into a single string.

Finally, the function uses the `print()` function to output the reversed string to the console.

Overall, this code demonstrates how to use the `reversed()` function and the `join()` method to reverse the order of characters in a string in Python.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/reverse_order_string.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

If the following string is given as input to the program:

```bash
rise to vote sir
```

Then, the output of the program should be:

```bash
ris etov ot esir
```

At this point, your code is running successfully!
