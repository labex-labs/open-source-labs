# Get Digit Words

Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/get_digit_words.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def get_digit_words():
    words = input().split()
    ans = []
    for word in words:
        if word.isdigit():       # can also use isnumeric() / isdecimal() function instead
            ans.append(word)
    print(ans)

    return ans


get_digit_words()

```

This Python code defines a function called `get_digit_words`. Within the function, the user is prompted to input a string of words.

The input string is then split into a list of words using the `split` method.

A new list `ans` is then generated using a `for` loop. The `for` loop iterates over each word in the list of words, and checks if the word is a digit using the `isdigit` method. If the word is a digit, it is added to the new list `ans`.

The resulting list of digit words is stored in the variable `ans`.

Finally, the resulting list is printed to the console using the `print` function, and also returned from the function.

Overall, this code demonstrates how to use a `for` loop and the `isdigit` method in Python to extract all digit words from a string of words entered by the user.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/get_digit_words.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

The following words is given as input to the program:

```bash
2 cats and 3 dogs.
```

Then, the output of the program should be:

```bash
['2', '3']
```

At this point, your code is running successfully!
