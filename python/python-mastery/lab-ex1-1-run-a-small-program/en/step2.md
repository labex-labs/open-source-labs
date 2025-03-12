# Create a Python Program File

Now that we've confirmed Python is working correctly, let's create a complete program file. In this step, we'll create a simple program that generates ASCII art patterns.

## Create the Program File

1. Open the WebIDE editor and create a new file called `art.py` in the `/home/labex/project` directory.

2. Copy the following code into the file:

   ```python
   # art.py

   import sys
   import random

   chars = '\|/'

   def draw(rows, columns):
       for r in range(rows):
           print(''.join(random.choice(chars) for _ in range(columns)))

   if __name__ == '__main__':
       if len(sys.argv) != 3:
           raise SystemExit("Usage: art.py rows columns")
       draw(int(sys.argv[1]), int(sys.argv[2]))
   ```

3. Save the file by pressing Ctrl+S or using the "Save" option in the File menu.

## Understanding the Code

Let's break down what this program does:

- `import sys` and `import random`: These lines import Python modules (libraries) that provide additional functionality.
- `chars = '\|/'`: This defines the character set that our art will use.
- The `draw()` function creates patterns with the specified number of rows and columns.
- The `if __name__ == '__main__':` block ensures the code only runs when the file is executed directly.
- `sys.argv` contains command-line arguments passed to the program.

## Run the Program

1. Open a terminal in your LabEx environment.

2. Run the program with the following command:

   ```bash
   python3 art.py 10 20
   ```

   This should attempt to generate a 10×20 pattern of characters.

3. You might notice that the program crashes with an error. Look carefully at the error message.

   The error occurs because the backslash (`\`) in the `chars` string has a special meaning in Python. It's used as an escape character.

## Fix the Program

1. Return to the editor and modify the `chars` line to fix the problem:

   ```python
   chars = '\\|/'  # Double backslash is needed to represent a literal backslash
   ```

   or alternatively:

   ```python
   chars = r'\|/'  # r prefix creates a "raw" string where backslashes aren't special
   ```

2. Save the file again.

## Run the Fixed Program

1. Run the program again:

   ```bash
   python3 art.py 10 20
   ```

2. This time, you should see output similar to this (your pattern will be different due to randomization):

   ```
   ||||/\||//\//\|||\|\
   ///||\/||\//|\\|\\/\
   |\////|//|||\//|/\||
   |//\||\/|\///|\|\|/|
   |/|//|/|/|\\/\/\||//
   |\/\|\//\\//\|\||\\/
   |||\\\\/\\\|/||||\/|
   \\||\\\|\||||////\\|
   //\//|/|\\|\//\|||\/
   \\\|/\\|/|\\\|/|/\/|
   ```

This program demonstrates:

- Reading command-line arguments
- Using random number generation
- String manipulation
- Creating functions
- Error handling

Try changing the numbers to get different sized patterns:

```bash
python3 art.py 5 40
```
