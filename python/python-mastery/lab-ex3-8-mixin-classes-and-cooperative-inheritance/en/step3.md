# Creating a User-Friendly API for Mixins

Mixins are powerful, but using multiple inheritance directly can feel complex. In this step, we'll improve the `create_formatter()` function to hide this complexity, providing an easier API for users.

First, ensure `tableformat.py` is open in your editor:

```bash
cd ~/project
touch tableformat.py
```

Find the existing `create_formatter()` function:

```python
# Existing function in tableformat.py
def create_formatter(name):
    """
    Create an appropriate formatter based on the name.
    """
    if name == 'text':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')
```

Replace the _entire existing_ `create_formatter()` function definition with the enhanced version below. This new version accepts optional arguments for column formats and uppercasing headers.

```python
# Replace the old create_formatter with this in tableformat.py

def create_formatter(name, column_formats=None, upper_headers=False):
    """
    Create a formatter with optional enhancements.

    Parameters:
    name : str
        Name of the formatter ('text', 'csv', 'html')
    column_formats : list, optional
        List of format strings for column formatting.
        Note: Relies on ColumnFormatMixin existing above this function.
    upper_headers : bool, optional
        Whether to convert headers to uppercase.
        Note: Relies on UpperHeadersMixin existing above this function.
    """
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {name}')

    # Build the inheritance list dynamically
    bases = []
    if column_formats:
        bases.append(ColumnFormatMixin)
    if upper_headers:
        bases.append(UpperHeadersMixin)
    bases.append(formatter_cls) # Base formatter class comes last

    # Create the custom class dynamically
    # Need to ensure ColumnFormatMixin and UpperHeadersMixin are defined before this point
    class CustomFormatter(*bases):
        # Set formats if ColumnFormatMixin is used
        if column_formats:
            formats = column_formats

    return CustomFormatter() # Return an instance of the dynamically created class
```

_Self-correction: Dynamically create the class tuple for inheritance instead of multiple if/elif branches._

This enhanced function first determines the base formatter class (`TextTableFormatter`, `CSVTableFormatter`, etc.). Then, based on the optional arguments `column_formats` and `upper_headers`, it dynamically constructs a new class (`CustomFormatter`) that inherits from the necessary mixins and the base formatter class. Finally, it returns an instance of this custom formatter.

**Remember to save the changes to `tableformat.py`.**

Now, let's test our enhanced function. **Make sure you have saved the updated `create_formatter` function in `tableformat.py`.**

First, test column formatting. Create `step3_test1.py`:

```python
# step3_test1.py
from tableformat import create_formatter, portfolio, print_table

# Using the same formats as before, subject to type issues.
# Use formats compatible with strings if '%d', '%.2f' cause errors.
formatter = create_formatter('text', column_formats=['%10s', '%10s', '%10.2f'])

print("--- Running Step 3 Test 1 (create_formatter with column_formats) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("--------------------------------------------------------------------")
```

Run the script:

```bash
python3 step3_test1.py
```

You should see the table with formatted columns (again, subject to the type handling of the price format):

```
--- Running Step 3 Test 1 (create_formatter with column_formats) ---
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
--------------------------------------------------------------------
```

Next, test uppercase headers. Create `step3_test2.py`:

```python
# step3_test2.py
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', upper_headers=True)

print("--- Running Step 3 Test 2 (create_formatter with upper_headers) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-------------------------------------------------------------------")
```

Run the script:

```bash
python3 step3_test2.py
```

You should see the table with uppercase headers:

```
--- Running Step 3 Test 2 (create_formatter with upper_headers) ---
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
-------------------------------------------------------------------
```

Finally, combine both options. Create `step3_test3.py`:

```python
# step3_test3.py
from tableformat import create_formatter, portfolio, print_table

# Using the same formats as before
formatter = create_formatter('text', column_formats=['%10s', '%10s', '%10.2f'], upper_headers=True)

print("--- Running Step 3 Test 3 (create_formatter with both options) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("------------------------------------------------------------------")
```

Run the script:

```bash
python3 step3_test3.py
```

This should display a table with both formatted columns and uppercase headers:

```
--- Running Step 3 Test 3 (create_formatter with both options) ---
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
------------------------------------------------------------------
```

The enhanced function also works with other formatter types. For example, try it with the CSV formatter. Create `step3_test4.py`:

```python
# step3_test4.py
from tableformat import create_formatter, portfolio, print_table

# For CSV, ensure formats produce valid CSV fields.
# Adding quotes around the string name field.
formatter = create_formatter('csv', column_formats=['"%s"', '%d', '%.2f'], upper_headers=True)

print("--- Running Step 3 Test 4 (create_formatter with CSV) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("---------------------------------------------------------")
```

Run the script:

```bash
python3 step3_test4.py
```

This should produce uppercase headers and formatted columns in CSV format (again, potential type issue for `%d`/`%.2f` formatting on strings passed from `print_table`):

```
--- Running Step 3 Test 4 (create_formatter with CSV) ---
NAME,SHARES,PRICE
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
---------------------------------------------------------
```

By enhancing the `create_formatter()` function, we've created a user-friendly API. Users can now easily apply mixin functionalities without needing to manage the multiple inheritance structure themselves.
