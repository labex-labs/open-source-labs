# Create a Simple Python Program

Now that we have confirmed Python is working correctly, let us create our first Python program file. We will start with a very simple program before moving to something more complex.

## Create Your First Python File

1. In the WebIDE, locate the Explorer panel on the left side of the screen.

2. Navigate to the `/home/labex/project` directory.

3. Right-click in the Explorer panel and select "New File".

4. Name the file `hello.py`.

5. In the editor, type the following code:

   ```python
   # This is a simple Python program

   name = input("Enter your name: ")
   print(f"Hello, {name}! Welcome to Python programming.")
   ```

6. Save the file by pressing Ctrl+S or by selecting File > Save from the menu.

## Run Your First Python Program

1. Open a terminal in the WebIDE if it is not already open.

2. Make sure you are in the correct directory:

   ```bash
   cd ~/project
   ```

3. Run your Python program by typing:

   ```bash
   python3 hello.py
   ```

4. When prompted, enter your name and press Enter.

5. You should see output similar to:

   ```
   Enter your name: John
   Hello, John! Welcome to Python programming.
   ```

   The actual output will show the name you entered instead of "John".

This simple program demonstrates:

- Creating a Python file
- Adding comments (the line starting with `#`)
- Getting user input with the `input()` function
- Using variables to store data
- Displaying output with the `print()` function
- Using f-strings for string formatting (the `f"Hello, {name}!"` part)
