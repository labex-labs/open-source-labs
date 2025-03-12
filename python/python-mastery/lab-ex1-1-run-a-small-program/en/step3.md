# Create a More Advanced Python Program

Now that you have grasped the basics of Python, it's time to take the next step and create a more advanced Python program. This program will generate ASCII art patterns, which are simple yet visually interesting designs made up of text characters. By working on this program, you'll get to learn and apply several important Python concepts, such as importing modules, defining functions, and handling command - line arguments.

## Create the ASCII Art Program

1. First, we need to open the `art.py` file in the WebIDE. This file was created during the setup process. You can find it in the `/home/labex/project` directory. Opening this file is the starting point for writing our ASCII art program.

2. Once the file is open, you'll notice that it might have some existing content. We need to clear that out because we're going to write our own code from scratch. So, delete any existing content in the file. Then, copy the following code into the `art.py` file. This code is the core of our ASCII art generator.

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

3. After you've copied the code into the file, it's important to save your work. You can do this by pressing Ctrl + S on your keyboard. Alternatively, you can go to the menu and select File > Save. Saving the file ensures that your code is stored and ready to be run.

## Understanding the Code

Let's take a closer look at what this program does. Understanding the code is crucial for you to be able to modify and expand it in the future.

- **Import Statements**: The lines `import sys` and `import random` are used to bring in Python's built - in modules. The `sys` module provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter. The `random` module allows us to generate random numbers, which we'll use to create random ASCII art patterns.
- **Character Set**: The line `chars = '\|/'` defines the set of characters that will be used to create our ASCII art. These characters will be randomly selected to form the patterns.
- **The `draw()` Function**: This function is responsible for creating the ASCII art patterns. It takes two arguments, `rows` and `columns`, which specify the dimensions of the pattern. Inside the function, it uses a loop to create each row of the pattern by randomly selecting characters from the `chars` set.
- **Main Block**: The `if __name__ == '__main__':` block is a special construct in Python. It ensures that the code inside this block only runs when the `art.py` file is executed directly. If the file is imported into another Python file, this code won't run.
- **Argument Handling**: The `sys.argv` variable contains the command - line arguments passed to the program. We check if exactly 3 arguments are provided (the name of the script itself plus two numbers representing the number of rows and columns). This helps us ensure that the user provides the correct input.
- **Error Handling**: The `try/except` block is used to catch errors that might occur. If the user provides invalid inputs, such as non - integer values for the rows and columns, the `try` block will raise a `ValueError`, and the `except` block will print an error message and exit the program.

## Run the Program

1. To run our program, we first need to open a terminal in the WebIDE. The terminal is where we'll enter commands to execute our Python script.

2. Once the terminal is open, we need to navigate to the project directory. This is where our `art.py` file is located. Use the following command in the terminal:

   ```bash
   cd ~/project
   ```

   This command changes the current working directory to the project directory.

3. Now that we're in the correct directory, we can run the program. Use the following command:

   ```bash
   python3 art.py 5 10
   ```

   This command tells Python to run the `art.py` script with 5 rows and 10 columns. When you run this command, you'll see a 5×10 pattern of characters printed in the terminal. The output will look something like this:

   ```
   |\//\\|\//
   /\\|\|//\\
   \\\/\|/|/\
   //|\\\||\|
   \|//|/\|/\
   ```

   Remember, the actual pattern is random, so your output will be different from the example shown here.

4. You can experiment with different dimensions by changing the arguments in the command. For example, try the following command:

   ```bash
   python3 art.py 8 15
   ```

   This will generate a larger pattern with 8 rows and 15 columns.

5. To see the error - handling in action, try providing invalid arguments. Run the following command:

   ```bash
   python3 art.py
   ```

   You should see an error message like this:

   ```
   Error: Incorrect number of arguments
   Usage: python3 art.py rows columns
   Example: python3 art.py 10 20
   ```

## Experiment with the Code

You can make the ASCII art patterns more interesting by modifying the character set. Here's how you can do it:

1. Open the `art.py` file again in the editor. This is where we'll make the changes to the code.

2. Find the `chars` variable in the code. Change it to use different characters. For example, you can use the following code:

   ```python
   chars = '*#@+.'
   ```

   This will change the set of characters used to create the ASCII art.

3. After making the change, save the file again using Ctrl + S or File > Save. Then, run the program with the following command:

   ```bash
   python3 art.py 5 10
   ```

   Now you'll see a different pattern using your new characters.

This exercise demonstrates several important Python concepts, including:

- Module imports: How to bring in additional functionality from Python's built - in modules.
- Function definition: How to define and use functions to organize your code.
- Command - line argument handling: How to accept and process user input from the command line.
- Error handling with try/except: How to handle errors gracefully in your program.
- String manipulation: How to create and manipulate strings to form the ASCII art patterns.
- Random number generation: How to generate random values to create unique patterns.
- List comprehensions: A concise way to create lists in Python, which is used in the `draw()` function.
