# Exploring the Dataset

Let's start our journey by taking a close look at the dataset we're going to work with. The file `ctabus.csv` is a CSV (Comma-Separated Values) file. CSV files are a common way to store tabular data, where each line represents a row, and the values within a row are separated by commas. This particular file holds daily ridership data for the Chicago Transit Authority (CTA) bus system, covering the period from January 1, 2001, to August 31, 2013.

To understand the structure of this file, we'll first peek inside it. We'll use Python to read the file and print out some lines. Open a terminal and run the following Python code:

```python
f = open('/home/labex/project/ctabus.csv')
print(next(f))  # Read the header line
print(next(f))  # Read the first data line
print(next(f))  # Read the second data line
f.close()
```

In this code, we first open the file using the `open` function and assign it to the variable `f`. The `next` function is used to read the next line from the file. We use it three times: the first time to read the header line, which usually contains the names of the columns in the dataset. The second and third times, we read the first and second data lines respectively. Finally, we close the file using the `close` method to free up system resources.

You should see output similar to this:

```
route,date,daytype,rides

3,01/01/2001,U,7354

4,01/01/2001,U,9288
```

This output shows that the file has 4 columns of data. Let's break down what each column represents:

1. `route`: This is the bus route name or number. It's the first column (Column 0) in the dataset.
2. `date`: It's a date string in the MM/DD/YYYY format. This is the second column (Column 1).
3. `daytype`: It's a day type code, which is the third column (Column 2).
   - U = Sunday/Holiday
   - A = Saturday
   - W = Weekday
4. `rides`: This column records the total number of riders as an integer. It's the fourth column (Column 3).

The `rides` column tells us how many people boarded a bus on a specific route on a given day. For example, from the output above, we can see that 7,354 people rode the number 3 bus on January 1, 2001.

Now, let's find out how many lines are in the file. Knowing the number of lines will give us an idea of the size of our dataset. Run the following Python code:

```python
with open('/home/labex/project/ctabus.csv') as f:
    line_count = sum(1 for line in f)
    print(f"Total lines in the file: {line_count}")
```

In this code, we use the `with` statement to open the file. The advantage of using `with` is that it automatically takes care of closing the file when we're done with it. We then use a generator expression `(1 for line in f)` to create a sequence of 1s, one for each line in the file. The `sum` function adds up all these 1s, giving us the total number of lines in the file. Finally, we print out the result.

This should output approximately 577,564 lines, which means we're dealing with a substantial dataset. This large dataset will provide us with plenty of data to analyze and draw insights from.
