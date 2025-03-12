# Create a More Advanced Python Program

Now that you understand the basics, let us create a more advanced Python program that generates ASCII art patterns. This program will demonstrate several important Python concepts including importing modules, defining functions, and handling command-line arguments.

## Create the ASCII Art Program

1. In the WebIDE, open the `art.py` file that was created during setup. You can find it in the `/home/labex/project` directory.

2. Delete any existing content and copy the following code into the file:

   ```python
   # art.py - A program to generate ASCII art patterns

   import sys
   import random

   # Characters used for the art pattern
   chars = '\|/'

   def draw(rows, columns):
       """
       Generate and print an ASCII art pattern with the specified dimensions.

       Args:
           rows: Number of rows in the pattern
           columns: Number of columns in the pattern
       """
       for r in range(rows):
           # For each row, create a string of random characters
           line = ''.join(random.choice(chars) for _ in range(columns))
           print(line)

   # This code only runs when the script is executed directly
   if __name__ == '__main__':
       # Check if the correct number of arguments was provided
       if len(sys.argv) != 3:
           print("Error: Incorrect number of arguments")
           print("Usage: python3 art.py rows columns")
           print("Example: python3 art.py 10 20")
           sys.exit(1)

       try:
           # Convert the arguments to integers
           rows = int(sys.argv[1])
           columns = int(sys.argv[2])

           # Call the draw function with the specified dimensions
           draw(rows, columns)
       except ValueError:
           print("Error: Both arguments must be integers")
           sys.exit(1)
   ```

3. Save the file by pressing Ctrl+S or selecting File > Save from the menu.

## Understanding the Code

Let us break down what this program does:

- **Import Statements**: `import sys` and `import random` include Python's built-in modules that provide additional functionality.
- **Character Set**: `chars = '\|/'` defines the characters that will be used in our ASCII art.
- **The `draw()` Function**: This function creates patterns with the specified number of rows and columns.
- **Main Block**: The `if __name__ == '__main__':` block ensures the code only runs when the file is executed directly (not when imported into another file).
- **Argument Handling**: `sys.argv` contains command-line arguments passed to the program. We check that exactly 3 arguments are provided (the script name plus two numbers).
- **Error Handling**: The `try/except` block catches errors that might occur if the user provides invalid inputs.

## Run the Program

1. Open a terminal in the WebIDE.

2. Navigate to the project directory:

   ```bash
   cd ~/project
   ```

3. Run the program with the following command:

   ```bash
   python3 art.py 5 10
   ```

   This generates a 5×10 pattern of characters. Your output will look something like:

   ```
   |\//\\|\//
   /\\|\|//\\
   \\\/\|/|/\
   //|\\\||\|
   \|//|/\|/\
   ```

   The actual pattern will be random, so your output will look different.

4. Try different dimensions by changing the arguments:

   ```bash
   python3 art.py 8 15
   ```

   You should see a larger pattern with 8 rows and 15 columns.

5. Try providing invalid arguments to see the error handling in action:

   ```bash
   python3 art.py
   ```

   You should see:

   ```
   Error: Incorrect number of arguments
   Usage: python3 art.py rows columns
   Example: python3 art.py 10 20
   ```

## Experiment with the Code

Try modifying the character set to create different patterns:

1. Open the `art.py` file again in the editor.

2. Change the `chars` variable to use different characters. For example:

   ```python
   chars = '*#@+.'
   ```

3. Save the file and run it again:

   ```bash
   python3 art.py 5 10
   ```

   Now you will see a different pattern using your new characters.

This exercise demonstrates important Python concepts including:

- Module imports
- Function definition
- Command-line argument handling
- Error handling with try/except
- String manipulation
- Random number generation
- List comprehensions
