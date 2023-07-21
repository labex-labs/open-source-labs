# Exercise 1.6: Debugging

The following code fragment contains code from the Sears tower problem. It also has a bug in it.

```python
# sears.py

bill_thickness = 0.11 * 0.001    # Meters (0.11 mm)
sears_height   = 442             # Height (meters)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = days + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
```

Copy and paste the code that appears above in a new program called `sears.py`.
When you run the code you will get an error message that causes the
program to crash like this:

```code
Traceback (most recent call last):
  File "sears.py", line 10, in <module>
    day = days + 1
NameError: name 'days' is not defined
```

Reading error messages is an important part of Python code. If your program
crashes, the very last line of the traceback message is the actual reason why the
the program crashed. Above that, you should see a fragment of source code and then
an identifying filename and line number.

- Which line is the error?
- What is the error?
- Fix the error
- Run the program successfully
