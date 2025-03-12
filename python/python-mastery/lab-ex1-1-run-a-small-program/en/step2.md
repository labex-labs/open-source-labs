# Create a Simple Python Program

Now that we have confirmed Python is working correctly, it's time to create our first Python program file. For beginners, it's always a good idea to start with something simple before moving on to more complex programs. This way, you can gradually understand the basic concepts and syntax of Python.

## Create Your First Python File

First, we'll create a new Python file. Here's how you can do it:

1. In the WebIDE, you'll notice a panel on the left side of the screen called the Explorer panel. This panel helps you navigate through different files and directories in your project. Locate this panel.

2. Once you've found the Explorer panel, you need to navigate to the `/home/labex/project` directory. This is where we'll store our Python program.

3. Right-click anywhere in the Explorer panel. A menu will appear. From this menu, select "New File". This action will create a new, empty file.

4. After creating the new file, you need to give it a name. Name the file `hello.py`. In Python, files usually have the `.py` extension, which indicates that they contain Python code.

5. Now, open the newly created `hello.py` file in the editor. In the editor, type the following code:

   ```python
   # This is a simple Python program

   name = input("Enter your name: ")
   print(f"Hello, {name}! Welcome to Python programming.")
   ```

   Let's break down this code. The line starting with `#` is a comment. Comments are used to explain what the code does and are ignored by the Python interpreter. The `input()` function is used to get user input. It displays the message "Enter your name: " and waits for the user to type something. The value entered by the user is then stored in the variable `name`. The `print()` function is used to display output on the screen. The `f"Hello, {name}!"` is an f-string, which is a convenient way to format strings in Python. It allows you to insert the value of a variable directly into a string.

6. After typing the code, you need to save the file. You can do this by pressing Ctrl+S on your keyboard or by selecting File > Save from the menu. Saving the file ensures that your changes are preserved.

## Run Your First Python Program

Now that you've created and saved your Python program, it's time to run it. Here's how:

1. Open a terminal in the WebIDE if it's not already open. The terminal allows you to execute commands and run programs.

2. Before running the Python program, you need to make sure you're in the correct directory. Type the following command in the terminal:

   ```bash
   cd ~/project
   ```

   This command changes the current working directory to the `project` directory in your home directory.

3. Once you're in the correct directory, you can run your Python program. Type the following command in the terminal:

   ```bash
   python3 hello.py
   ```

   This command tells the Python interpreter to run the `hello.py` file.

4. When the program runs, it will prompt you to enter your name. Type your name and press Enter.

5. After you press Enter, you should see output similar to:

   ```
   Enter your name: John
   Hello, John! Welcome to Python programming.
   ```

   The actual output will show the name you entered instead of "John".

This simple program demonstrates several important concepts in Python:

- Creating a Python file: You learned how to create a new Python file in the WebIDE.
- Adding comments: Comments are used to explain the code and make it more understandable.
- Getting user input with the `input()` function: This function allows your program to interact with the user.
- Using variables to store data: Variables are used to store values that can be used later in the program.
- Displaying output with the `print()` function: This function is used to show information on the screen.
- Using f-strings for string formatting: F-strings provide a convenient way to insert variables into strings.
