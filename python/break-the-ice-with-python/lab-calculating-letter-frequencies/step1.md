# Calculating Letter Frequencies

You are given a string.Your task is to count the frequency of letters of the string and print the letters in descending order of frequency.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/calculating_letter_frequencies.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def calculating_letter_frequencies():
    word = input()
    dct = {}
    for i in word:
        dct[i] = dct.get(i, 0) + 1

    dct = sorted(dct.items(), key=lambda x: (-x[1], x[0]))
    for i in dct:
        print(i[0], i[1])


calculating_letter_frequencies()

```

This Python code defines a function called `calculating_letter_frequencies` that calculates the frequency of each letter in an input word and prints them in descending order of frequency and ascending order of letters. It uses a dictionary to store the frequency of each letter and sorts the dictionary using the `sorted()` function and a `lambda` expression. Finally, it prints the sorted dictionary to the console.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/calculating_letter_frequencies.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

If the following string is given as input to the program:

```bash
aabbbccde
```

Then, the output of the program should be:

```bash
b 3
a 2
c 2
d 1
e 1
```

At this point, your code is running successfully!
