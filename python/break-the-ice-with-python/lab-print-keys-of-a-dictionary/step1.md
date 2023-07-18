# Print Keys of a Dictionary

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/print_keys_of_a_dictionary.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def print_keys_of_a_dictionary():
    dict = {i: i**2 for i in range(1, 21)}
    print(dict.keys())      # print keys of a dictionary


print_keys_of_a_dictionary()

```

This Python code defines a function called `print_keys_of_a_dictionary`. Within the function, a dictionary `dict` is initialized with keys and values using a dictionary comprehension.

The dictionary comprehension creates a dictionary where the keys are integers from 1 to 20, and the values are the squares of the keys.

The `keys` method is then used to obtain a view object of the keys in the dictionary. The `view` object is then printed to the console using the `print` function.

Overall, this code demonstrates how to use dictionary comprehensions and the `keys` method in Python to create a dictionary and print its keys.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/print_keys_of_a_dictionary.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
dict_keys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
```

At this point, your code is running successfully!
