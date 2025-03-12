# Verify Python Installation and Use the Interactive Interpreter

The Python interactive interpreter is a very useful tool. It lets you run Python code one line at a time and see the results right away. This is great for beginners because you can test small pieces of code without having to write a whole program. Before we start writing full - fledged programs, we need to make sure Python is installed correctly on your system. Then, we'll learn how to use this interpreter to execute Python code.

## Launch the Python Interpreter

1. First, we need to open a terminal in the WebIDE. The terminal is like a command - center where you can type in commands to interact with your computer. You'll find a terminal tab at the bottom of the screen. Once you open it, you're ready to start typing commands.

2. In the terminal, we're going to check if Python is installed and which version you have. Type the following command and then press Enter:

   ```bash
   python3 --version
   ```

   This command asks your system to show you the version of Python that is currently installed. If Python is installed correctly, you'll see output similar to:

   ```
   Python 3.10.x
   ```

   The `x` here represents a specific patch number, which can vary depending on your installation.

3. Now that we know Python is installed, let's start the Python interactive interpreter. Type the following command in the terminal and press Enter:

   ```bash
   python3
   ```

   After you press Enter, you'll see some information about the Python version and other details. The output will look something like this:

   ```
   Python 3.10.x (default, ...)
   [GCC x.x.x] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>>
   ```

   The `>>>` prompt is a signal that the Python interpreter is up and running and is waiting for you to enter Python commands.

## Try Simple Python Commands

Now that the Python interpreter is running, let's try out some basic Python commands. These commands will help you understand how Python works and how to use the interpreter.

1. At the `>>>` prompt, type the following command and press Enter:

   ```python
   >>> print('Hello World')
   ```

   The `print` function in Python is used to display text on the screen. When you run this command, you'll see the following output:

   ```
   Hello World
   >>>
   ```

   This shows that the `print` function has successfully displayed the text 'Hello World'.

2. Let's try a simple math calculation. At the prompt, type:

   ```python
   >>> 2 + 3
   ```

   Python will automatically evaluate this expression and show you the result. You'll see:

   ```
   5
   >>>
   ```

   This demonstrates that Python can perform basic arithmetic operations.

3. Next, we'll create a variable and use it. Variables in Python are used to store data. Type the following commands at the prompt:

   ```python
   >>> message = "Learning Python"
   >>> print(message)
   ```

   In the first line, we're creating a variable named `message` and storing the string "Learning Python" in it. In the second line, we're using the `print` function to display the value stored in the `message` variable. The output will be:

   ```
   Learning Python
   >>>
   ```

   The Python interpreter executes each line of code as soon as you enter it. This makes it a great tool for quickly testing ideas and learning Python concepts.

## Exit the Interpreter

When you're done experimenting with the Python interpreter, you can exit it using one of the following methods:

1. You can type the following command at the `>>>` prompt and press Enter:

   ```python
   >>> exit()
   ```

   Or you can use this alternative command:

   ```python
   >>> quit()
   ```

   Both of these commands tell the Python interpreter to stop running and return you to the regular terminal.

2. Another way to exit is by pressing Ctrl+D on your keyboard. This is a shortcut that also stops the Python interpreter.

After you exit the interpreter, you'll return to the regular terminal prompt, where you can run other commands on your system.
