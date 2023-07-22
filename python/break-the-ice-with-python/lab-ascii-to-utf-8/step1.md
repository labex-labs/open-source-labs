# ASCII to UTF-8

Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/ascii_to_utf_8.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def ascii_to_utf_8():
    s = input()
    u = s.encode('utf-8')
    print(u)

    return u


ascii_to_utf_8()

```

This Python code defines a function called `ascii_to_utf_8` which uses the `input()` function to prompt the user to enter an `ASCII` string, then uses `encode()` function to convert it to `UTF-8` encoding, and prints the result. The return value of the function is the converted `UTF-8` string. Finally, the code calls the function to perform the conversion operation.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/ascii_to_utf_8.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Type the following words in the terminal:

```bash
python
```

Then, the output of the program should be:

```bash
b'python'
```

At this point, your code is running successfully!
