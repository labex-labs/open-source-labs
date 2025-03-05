# Understanding Date Objects in Python

Before calculating the month difference between dates, we need to understand how to work with date objects in Python. In this step, we will learn about the `datetime` module and create some date objects.

First, let's create a new Python file in the project directory. Open the WebIDE and click on the "New File" icon in the explorer panel on the left side. Name the file `month_difference.py` and save it in the `/home/labex/project` directory.

Now add the following code to import the necessary modules:

```python
from datetime import date
from math import ceil

# Create example date objects
date1 = date(2023, 1, 15)  # January 15, 2023
date2 = date(2023, 3, 20)  # March 20, 2023

# Print the dates to see their format
print(f"Date 1: {date1}")
print(f"Date 2: {date2}")

# Calculate the difference in days
day_difference = (date2 - date1).days
print(f"Difference in days: {day_difference}")
```

Save the file and run it using the terminal:

```bash
python3 ~/project/month_difference.py
```

You should see output similar to this:

```
Date 1: 2023-01-15
Date 2: 2023-03-20
Difference in days: 64
```

The `date` class from the `datetime` module allows us to create date objects by specifying the year, month, and day. When we subtract one date from another, Python returns a `timedelta` object. We can access the number of days in this object using the `.days` attribute.

In this example, there are 64 days between January 15, 2023, and March 20, 2023.
