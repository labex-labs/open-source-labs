# Word Counting

You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/word_counting.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def word_counting():
    n = int(input())

    word_list = []
    word_dict = {}

    for i in range(n):
        word = input()
        if word not in word_dict:
            word_list.append(word)
        word_dict[word] = word_dict.get(word, 0) + 1

    print(len(word_list))
    for word in word_list:
        print(word_dict[word], end=' ')


word_counting()

```

This Python code defines a function called `word_counting()` that counts the number of unique words in a list of words and prints the frequency of each word. The function prompts the user to input an integer `n` representing the number of words in the list.

The function then initializes two empty data structures: a list called `word_list` to store the unique words in the list, and a dictionary called `word_dict` to store the frequency of each word.

The function then uses a `for` loop to iterate `n` times and prompt the user to input a word. If the word is not already in the `word_dict`, it is added to the `word_list`. The frequency of the word in the `word_dict` is then incremented by 1 using the `get()` method.

Finally, the function prints the number of unique words in the `word_list` using the `len()` function, followed by the frequency of each word in the `word_list` using another `for` loop. The frequency of each word is retrieved from the `word_dict` using the `get()` method and printed to the console using the `print()` function with the `end` parameter set to a space character to separate the frequencies.

The `word_counting()` function is then called to execute it and prompt the user for input.

Overall, this code demonstrates how to count the frequency of words in a list using a dictionary in Python. It also shows how to use a `for` loop to iterate over a range of numbers and prompt the user for input.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/word_counting.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

If the following string is given as input to the program:

```bash
4
bcdef
abcdefg
bcde
bcdef
```

Then, the output of the program should be:

```bash
3
2 1 1
```

At this point, your code is running successfully!
