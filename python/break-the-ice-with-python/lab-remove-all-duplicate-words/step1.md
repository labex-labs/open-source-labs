# Remove all Duplicate Words

Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/remove_all_duplicate_words.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def remove_all_duplicate_words():
    word = input().split()

    for i in word:
        # count function returns total repeatation of an element that is send as argument
        if word.count(i) > 1:
            word.remove(i)     # removes exactly one element per call

    word.sort()
    print(" ".join(word))


remove_all_duplicate_words()

```

This Python code defines a function called `remove_all_duplicate_words` that removes duplicate words from a list of words. The function prompts the user to input a list of words, which are then stored in a list called `word`. The function then iterates over each word in the list and uses the `count()` function to determine how many times that word appears in the list. If the count is greater than 1, meaning the word appears more than once, the function uses the `remove()` function to remove one instance of that word from the list. This process continues until there are no more duplicate words in the list. Finally, the function sorts the list in alphabetical order and uses the `join()` function to concatenate the words into a single string separated by spaces. The resulting string is then printed to the console.

In summary, this code demonstrates how to remove duplicate words from a list of words in Python using the `count()` and `remove()` functions, and how to sort and concatenate the resulting list into a single string using the `sort()` and `join()` functions.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/remove_all_duplicate_words.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
hello world and practice makes perfect and hello world again
```

Then, the output of the program should be:

```bash
again and hello makes perfect practice world
```

At this point, your code is running successfully!
