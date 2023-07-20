# Print each Even Numbers

Write a program, which will find all such numbers between 1000 and 2200 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/print_each_even_numbers.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def print_each_even_numbers():
    lst = []

    for i in range(1000, 2201):
        flag = 1
        for j in str(i):          # every integer number i is converted into string
            if ord(j) % 2 != 0:     # ord returns ASCII value and j is every digit of i
                flag = 0          # flag becomes zero if any odd digit found
        if flag == 1:
            lst.append(str(i))    # i is stored in list as string

    print(",".join(lst))


print_each_even_numbers()

```

This Python code defines a function called `print_each_even_numbers`. Within the function, an empty list `lst` is created.

A `for` loop is then used to iterate over a of integers from 1000 to 2200. Within the loop, a variable `flag` is initialized to 1.

Another `for` loop is used to iterate over each digit of the current integer `i`. The `ord` function is used to obtain the ASCII value of the digit, and the `%` operator is used to check if the digit is even or odd. If any odd digit is found, the `flag` variable is set to 0.

If the `flag` variable is still 1 after checking all the digits of `i`, then `i` is appended to the `lst` list as a string.

Finally, the elements of the `lst` list are joined together using the `join` method with the `,` character as the separator, and the resulting string is printed to the console using the `print` function.

Overall, this code demonstrates how to use loops and string manipulation in Python to find and print all even numbers between 1000 and 2200 whose digits are all even.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/print_each_even_numbers.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
2000,2002,2004,2006,2008,2020,2022,2024,2026,2028,2040,2042,2044,2046,2048,2060,2062,2064,2066,2068,2080,2082,2084,2086,2088,2200
```

At this point, your code is running successfully!
