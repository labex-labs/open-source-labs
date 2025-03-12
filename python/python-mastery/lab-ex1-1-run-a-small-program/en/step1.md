# Verify Python Installation and Use the Interactive Interpreter

The Python interactive interpreter is a powerful tool that allows you to execute Python code line by line and see immediate results. Before writing complete programs, let us first make sure Python is correctly installed and learn how to use this interpreter.

## Launch the Python Interpreter

1. First, open a terminal in the WebIDE. You should see a terminal tab at the bottom of the screen.

2. In the terminal, type the following command and press Enter:

   ```bash
   python3 --version
   ```

   This command displays the installed Python version. You should see output similar to:

   ```
   Python 3.10.x
   ```

3. Now, let us start the Python interactive interpreter by typing:

   ```bash
   python3
   ```

   You will see output similar to:

   ```
   Python 3.10.x (default, ...)
   [GCC x.x.x] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>>
   ```

   The `>>>` prompt indicates that Python is ready to accept commands.

## Try Simple Python Commands

Let us experiment with some basic Python commands:

1. Type the following at the prompt and press Enter:

   ```python
   >>> print('Hello World')
   ```

   You will see:

   ```
   Hello World
   >>>
   ```

2. Try a simple math calculation:

   ```python
   >>> 2 + 3
   ```

   Python will evaluate and display the result:

   ```
   5
   >>>
   ```

3. Create a variable and use it:

   ```python
   >>> message = "Learning Python"
   >>> print(message)
   ```

   Output:

   ```
   Learning Python
   >>>
   ```

The Python interpreter immediately executes each line of code as you enter it, making it perfect for testing ideas and learning Python concepts.

## Exit the Interpreter

When you finish experimenting with the Python interpreter, you can exit it using one of these methods:

1. Type the following command and press Enter:

   ```python
   >>> exit()
   ```

   Or you can use:

   ```python
   >>> quit()
   ```

2. Alternatively, press Ctrl+D on your keyboard.

You will return to the regular terminal prompt after exiting the interpreter.
