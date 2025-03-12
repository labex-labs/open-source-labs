# Working with Structured Data using Tuples

So far, we've looked at storing raw text data. However, for data analysis, we typically want to parse the data into more structured formats. In this step, we'll explore how to read the data as a list of tuples using the `csv` module.

## Creating a Reader Function with Tuples

Let's create a new file called `readrides.py` in the `/home/labex/project` directory:

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

This script defines a function `read_rides_as_tuples` that:

1. Opens the CSV file
2. Uses the `csv` module to parse each line
3. Extracts the four fields from each row
4. Converts the 'rides' field to an integer
5. Creates a tuple with these values
6. Adds the tuple to a list of records

Run the script:

```bash
python3 /home/labex/project/readrides.py
```

You should see output similar to:

```
Number of records: 577563
First record: ('3', '01/01/2001', 'U', 7354)
Second record: ('4', '01/01/2001', 'U', 9288)
Memory Use: Current 89.12 MB, Peak 89.15 MB
```

Notice how the memory usage has increased compared to our previous examples. This is because:

1. We're now storing the data in a structured format (tuples)
2. Each value in the tuple is a separate Python object
3. We have an additional list structure holding all these tuples

The advantage of this approach is that our data is now properly structured and ready for analysis. We can easily access specific fields of each record by index:

```python
# Example of accessing tuple elements (add this to readrides.py file to try it)
first_record = rows[0]
route = first_record[0]
date = first_record[1]
daytype = first_record[2]
rides = first_record[3]
print(f"Route: {route}, Date: {date}, Day type: {daytype}, Rides: {rides}")
```

However, accessing data by numeric index isn't always intuitive. In the next step, we'll explore other data structures that can make our code more readable and maintainable.
