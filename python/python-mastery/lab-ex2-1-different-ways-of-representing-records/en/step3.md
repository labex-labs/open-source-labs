# Working with Structured Data using Tuples

So far, we've been dealing with storing raw text data. But when it comes to data analysis, we usually need to transform the data into more organized and structured formats. This makes it easier to perform various operations and gain insights from the data. In this step, we'll learn how to read data as a list of tuples using the `csv` module. Tuples are a simple and useful data structure in Python that can hold multiple values.

## Creating a Reader Function with Tuples

Let's create a new file named `readrides.py` in the `/home/labex/project` directory. This file will contain the code to read the data from a CSV file and store it as a list of tuples.

```python
# readrides.py
import csv
import tracemalloc

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    tracemalloc.start()

    rows = read_rides_as_tuples('/home/labex/project/ctabus.csv')

    current, peak = tracemalloc.get_traced_memory()
    print(f'Number of records: {len(rows)}')
    print(f'First record: {rows[0]}')
    print(f'Second record: {rows[1]}')
    print(f'Memory Use: Current {current/1024/1024:.2f} MB, Peak {peak/1024/1024:.2f} MB')
```

This script defines a function called `read_rides_as_tuples`. Here's what it does step by step:

1. It opens the CSV file specified by the `filename` parameter. This allows us to access the data inside the file.
2. It uses the `csv` module to parse each line of the file. The `csv.reader` function helps us split the lines into individual values.
3. It extracts the four fields (route, date, day type, and number of rides) from each row. These fields are important for our data analysis.
4. It converts the 'rides' field to an integer. This is necessary because the data in the CSV file is initially in string format, and we need a numeric value for calculations.
5. It creates a tuple with these four values. Tuples are immutable, which means their values cannot be changed once they are created.
6. It adds the tuple to a list called `records`. This list will hold all the records from the CSV file.

Now, let's run the script. Open your terminal and enter the following command:

```bash
python3 /home/labex/project/readrides.py
```

You should see output similar to this:

```
Number of records: 577563
First record: ('3', '01/01/2001', 'U', 7354)
Second record: ('4', '01/01/2001', 'U', 9288)
Memory Use: Current 89.12 MB, Peak 89.15 MB
```

Notice that the memory usage has increased compared to our previous examples. There are a few reasons for this:

1. We're now storing the data in a structured format (tuples). Structured data usually requires more memory because it has a defined organization.
2. Each value in the tuple is a separate Python object. Python objects have some overhead, which contributes to the increased memory usage.
3. We have an additional list structure that holds all these tuples. Lists also take up memory to store their elements.

The advantage of using this approach is that our data is now properly structured and ready for analysis. We can easily access specific fields of each record by index. For example:

```python
# Example of accessing tuple elements (add this to readrides.py file to try it)
first_record = rows[0]
route = first_record[0]
date = first_record[1]
daytype = first_record[2]
rides = first_record[3]
print(f"Route: {route}, Date: {date}, Day type: {daytype}, Rides: {rides}")
```

However, accessing data by numeric index isn't always intuitive. It can be difficult to remember which index corresponds to which field, especially when dealing with a large number of fields. In the next step, we'll explore other data structures that can make our code more readable and maintainable.
