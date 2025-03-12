# Exploring the Dataset

Let's begin by examining the dataset we'll be working with. The file `ctabus.csv` is a CSV (Comma-Separated Values) file containing daily ridership data for the Chicago Transit Authority (CTA) bus system from January 1, 2001 to August 31, 2013.

First, let's look at the file to understand its structure. Open a terminal and run the following Python code:

```python
f = open('/home/labex/project/ctabus.csv')
print(next(f))  # Read the header line
print(next(f))  # Read the first data line
print(next(f))  # Read the second data line
f.close()
```

You should see output similar to this:

```
route,date,daytype,rides

3,01/01/2001,U,7354

4,01/01/2001,U,9288
```

This shows that the file contains 4 columns of data:

1. `route`: The bus route name/number (Column 0)
2. `date`: A date string in MM/DD/YYYY format (Column 1)
3. `daytype`: A day type code (Column 2)
   - U = Sunday/Holiday
   - A = Saturday
   - W = Weekday
4. `rides`: Total number of riders as an integer (Column 3)

The `rides` column records the total number of people who boarded a bus on that route on a given day. For example, from the output above, 7,354 people rode the number 3 bus on January 1, 2001.

Let's check how many lines are in the file to understand the size of our dataset:

```python
with open('/home/labex/project/ctabus.csv') as f:
    line_count = sum(1 for line in f)
    print(f"Total lines in the file: {line_count}")
```

This should output approximately 577,564 lines, indicating a substantial dataset that we'll be working with.
