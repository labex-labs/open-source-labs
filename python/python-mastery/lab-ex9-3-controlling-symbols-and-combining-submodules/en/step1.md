# Understanding Package Import Complexity

When you start working with Python packages, you'll quickly realize that importing modules can get quite complicated and wordy. This complexity can make your code harder to read and write. In this lab, we'll take a close look at this issue and learn how to simplify the import process.

## Current Import Structure

First, let's open the terminal. The terminal is a powerful tool that allows you to interact with your computer's operating system. Once the terminal is open, we need to navigate to the project directory. The project directory is where all the files related to our Python project are stored. To do this, we'll use the `cd` command, which stands for "change directory".

```bash
cd ~/project
```

Now that we're in the project directory, let's examine the current structure of the `structly` package. A package in Python is a way to organize related modules. We can use the `ls -la` command to list all the files and directories within the `structly` package, including hidden files.

```bash
ls -la structly
```

You'll notice that there are several Python modules inside the `structly` package. These modules contain functions and classes that we can use in our code. However, if we want to use the functionality from these modules, we currently need to use long import statements. For example:

```python
from structly.structure import Structure
from structly.reader import read_csv_as_instances
from structly.tableformat import create_formatter, print_table
```

These long import paths can be a hassle to write, especially if you need to use them multiple times in your code. They also make your code less readable, which can be a problem when you're trying to understand or debug your code. In this lab, we'll learn how to organize the package in a way that makes these imports simpler.

Let's start by looking at the content of the package's `__init__.py` file. The `__init__.py` file is a special file in Python packages. It's executed when the package is imported, and it can be used to initialize the package and set up any necessary imports.

```bash
cat structly/__init__.py
```

You'll likely find that the `__init__.py` file is either empty or contains very little code. In the next steps, we'll modify this file to simplify our import statements.

## The Goal

By the end of this lab, our goal is to be able to use much simpler import statements. Instead of the long import paths we saw earlier, we'll be able to use statements like:

```python
from structly import Structure, read_csv_as_instances, create_formatter, print_table
```

Or even:

```python
from structly import *
```

Using these simpler import statements will make our code cleaner and easier to work with. It will also save us time and effort when writing and maintaining our code.
