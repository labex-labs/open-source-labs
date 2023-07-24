# the Frequency of the Words

Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/the_frequency_of_the_words.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def the_frequency_of_the_words():
    ss = input().split()
    word = sorted(set(ss))     # split words are stored and sorted as a set

    for i in word:
        print("{0}:{1}".format(i, ss.count(i)))


the_frequency_of_the_words()

```

This Python code defines a function called `the_frequency_of_the_words()` that calculates the frequency of each word in a given string. The function prompts the user to input a string using the `input()` function and splits it into a list of words using the `split()` function.

The function then creates a set of unique words from the list using the `set()` function and sorts them in alphabetical order using the `sorted()` function.

The function then uses a for loop to iterate over each word in the sorted set and prints the word and its frequency in the original string to the console using the `print()` function and the `count()` method.

Finally, the `the_frequency_of_the_words()` function is called to execute it and prompt the user for input.

Overall, this code demonstrates how to split a string into words, count the frequency of each word, and print the results to the console in Python. It also shows how to use the `set()` and `sorted()` functions to create a sorted set of unique words from a list.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/the_frequency_of_the_words.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
```

Then, the output of the program should be:

```bash
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
```

At this point, your code is running successfully!
