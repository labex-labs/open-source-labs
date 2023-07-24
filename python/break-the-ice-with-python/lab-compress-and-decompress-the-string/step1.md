# Compress and Decompress the String

Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

## Preparation

Before we start writing the code, we should open the `/home/labex/project/compress_and_decompress_the_string.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
import zlib


def compress_and_decompress_the_string():
    s = 'hello world!hello world!hello world!hello world!'
    # In Python 3 zlib.compress() accepts only DataType <bytes>
    y = bytes(s, 'utf-8')
    x = zlib.compress(y)
    print(x)
    print(zlib.decompress(x))


compress_and_decompress_the_string()

```

This Python code demonstrates how to use Python's `zlib` module to compress and decompress strings. First, a function named `compress_and_decompress_the_string` is defined, which contains a string `s` that is assigned the value of `'hello world!hello world!hello world!hello world!'`.

Next, the `bytes` function is used to convert the `s` string to bytes and assign it to the variable `y`. Then, the `zlib.compress` function is used to compress `y`, and the result is assigned to the variable `x`. Finally, the `print` function is used to print `x` to the console, and the `zlib.decompress` function is used to decompress `x`, with the result also printed to the console.

Overall, this code demonstrates how to use Python's `zlib` module to compress and decompress strings. It first converts the string to bytes, then uses the `zlib.compress` function to compress it, and uses the `zlib.decompress` function to decompress the compressed data.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/compress_and_decompress_the_string.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaIQ\xcc \x82\r\x00\xbd[\x11\xf5'
b'hello world!hello world!hello world!hello world!'
```

At this point, your code is running successfully!
