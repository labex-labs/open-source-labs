# Determine what Day of the Week

You are given a date. Your task is to find what the day is on that date.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/determine_what_day_of_the_week.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
import calendar


def determine_what_day_of_the_week():
    month, day, year = map(int, input().split())

    dayId = calendar.weekday(year, month, day)
    print(calendar.day_name[dayId].upper())


determine_what_day_of_the_week()

```

This Python code imports the `calendar` module, which provides functions for working with calendars, including determining the day of the week for a given date.

The `determine_what_day_of_the_week` function is defined, which prompts the user to enter a date in the format of "month day year". The `input` function is used to read the user's input, and the `map` function is used to convert the input values to integers.

The `weekday` function from the `calendar` module is then used to determine the day of the week for the given date. The function takes three arguments: the year, month, and day of the date. It returns an integer representing the day of the week, where Monday is 0 and Sunday is 6.

Finally, the `day_name` attribute of the `calendar` module is used to get the name of the day of the week corresponding to the integer returned by `weekday`. The name is converted to uppercase using the `upper` method, and then printed to the console using the `print` function.

Overall, this code demonstrates how to use the `calendar` module in Python to determine the day of the week for a given date. It also shows how to use the `input` function to read user input and the `map` function to convert the input values to integers.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/determine_what_day_of_the_week.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
08 05 2015
```

Then, output the correct day in capital letters:

```bash
WEDNESDAY
```

At this point, your code is running successfully!
