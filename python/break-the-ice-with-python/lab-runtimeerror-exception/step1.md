# RuntimeError Exception

Please raise a `RuntimeError` exception.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/runtimeerror_exception.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
raise RuntimeError('something wrong')
```

This Python code raises a `RuntimeError` exception with the message "something wrong". The `raise` keyword is used to raise an exception in Python. In this case, the `RuntimeError exception is raised with the message "something wrong".

When an exception is raised, the program execution is immediately halted and the exception is propagated up the call stack until it is caught by an exception handler. If there is no exception handler that can handle the exception, the program will terminate with an error message.

Overall, this code demonstrates how to raise an exception in Python using the `raise` keyword. The `RuntimeError` exception is a built-in exception in Python that can be used to indicate a generic runtime error.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/runtimeerror_exception.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program may be:

```bash
RuntimeError: something wrong
```

At this point, your code is running successfully!
