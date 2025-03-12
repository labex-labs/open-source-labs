# Understanding Package Import Complexity

When working with Python packages, you might notice that imports can become complex and verbose. Let's examine this problem and learn how to solve it.

## Current Import Structure

Open your terminal and navigate to the project directory:

```bash
cd ~/project
```

Let's look at the current structure of the `structly` package:

```bash
ls -la structly
```

You'll see several Python modules within the `structly` package. Currently, if we want to use functionality from these modules, we need import statements like:

```python
from structly.structure import Structure
from structly.reader import read_csv_as_instances
from structly.tableformat import create_formatter, print_table
```

These long import paths can become cumbersome to write and make code less readable. In this lab, we'll learn how to organize the package for simpler imports.

Let's first examine the content of the package's `__init__.py` file:

```bash
cat structly/__init__.py
```

You'll see that it's likely empty or contains minimal code. In the next steps, we'll modify this file to simplify imports.

## The Goal

By the end of this lab, we'll be able to use simpler import statements like:

```python
from structly import Structure, read_csv_as_instances, create_formatter, print_table
```

Or even:

```python
from structly import *
```

This will make our code cleaner and easier to work with.
