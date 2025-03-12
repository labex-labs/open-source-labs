# Data Analysis Challenge with Chicago Transit Authority Data

Now that you've practiced working with different Python data structures and the collections module, it's time to put these skills to use in a real - world data analysis task. In this experiment, we'll be analyzing the bus ridership data from the Chicago Transit Authority (CTA). This practical application will help you understand how to use Python to extract meaningful information from real - world datasets.

## Understanding the Data

First, let's take a look at the transit data we'll be working with. In your Python terminal, you'll run some code to load the data and understand its basic structure.

```python
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('/home/labex/project/ctabus.csv')
>>> print(len(rows))
# This will show the number of records in the dataset

>>> # Let's look at the first record to understand the structure
>>> import pprint
>>> pprint.pprint(rows[0])
```

The `import readrides` statement imports a custom module that has a function to read the data from the CSV file. The `readrides.read_rides_as_dicts` function reads the data from the specified CSV file and converts each row into a dictionary. The `len(rows)` gives us the total number of records in the dataset. By printing the first record using `pprint.pprint(rows[0])`, we can see the structure of each record clearly.

The data contains daily ridership records for different bus routes. Each record includes:

- `route`: The bus route number
- `date`: The date in format "YYYY - MM - DD"
- `daytype`: Either "W" for weekday, "A" for Saturday, or "U" for Sunday/holiday
- `rides`: The number of riders that day

## Analysis Tasks

Let's solve each of the challenge questions one by one:

### Question 1: How many bus routes exist in Chicago?

To answer this question, we need to find all the unique route numbers in the dataset. We'll use a set comprehension for this task.

```python
>>> # Get all unique route numbers using a set comprehension
>>> unique_routes = {row['route'] for row in rows}
>>> print(len(unique_routes))
```

A set comprehension is a concise way to create a set. In this case, we iterate over each row in the `rows` list and extract the `route` value. Since a set only stores unique elements, we end up with a set of all unique route numbers. Printing the length of this set gives us the total number of unique bus routes.

We can also see what some of these routes are:

```python
>>> # Print a few of the route numbers
>>> print(list(unique_routes)[:10])
```

Here, we convert the set of unique routes to a list and then print the first 10 elements of that list.

### Question 2: How many people rode the number 22 bus on February 2, 2011?

For this question, we need to filter the data to find the specific record that matches the given route and date.

```python
>>> # Find rides on route 22 on February 2, 2011
>>> target_date = "2011-02-02"
>>> target_route = "22"
>>>
>>> for row in rows:
...     if row['route'] == target_route and row['date'] == target_date:
...         print(f"Rides on route {target_route} on {target_date}: {row['rides']}")
...         break
```

We first define the `target_date` and `target_route` variables. Then, we iterate over each row in the `rows` list. For each row, we check if the `route` and `date` match our target values. If a match is found, we print the number of rides and break out of the loop since we've found the record we're looking for.

You can modify this to check any route on any date by changing the `target_date` and `target_route` variables.

### Question 3: What is the total number of rides taken on each bus route?

Let's use a Counter to calculate the total rides per route. A Counter is a dictionary subclass from the `collections` module that's used to count hashable objects.

```python
>>> from collections import Counter
>>>
>>> # Initialize a counter
>>> total_rides_by_route = Counter()
>>>
>>> # Sum up rides for each route
>>> for row in rows:
...     total_rides_by_route[row['route']] += row['rides']
...
>>> # View the top 5 routes by total ridership
>>> for route, rides in total_rides_by_route.most_common(5):
...     print(f"Route {route}: {rides:,} total rides")
```

We first import the `Counter` class from the `collections` module. Then, we initialize an empty counter called `total_rides_by_route`. As we iterate over each row in the `rows` list, we add the number of rides for each route to the counter. Finally, we use the `most_common(5)` method to get the top 5 routes with the highest total ridership and print the results.

### Question 4: What five bus routes had the greatest ten - year increase in ridership from 2001 to 2011?

This is a more complex task. We need to compare the ridership in 2001 with that in 2011 for each route.

```python
>>> # Create dictionaries to store total annual rides by route
>>> rides_2001 = Counter()
>>> rides_2011 = Counter()
>>>
>>> # Collect data for each year
>>> for row in rows:
...     if row['date'].startswith('2001-'):
...         rides_2001[row['route']] += row['rides']
...     elif row['date'].startswith('2011-'):
...         rides_2011[row['route']] += row['rides']
...
>>> # Calculate increases
>>> increases = {}
>>> for route in unique_routes:
...     if route in rides_2001 and route in rides_2011:
...         increase = rides_2011[route] - rides_2001[route]
...         increases[route] = increase
...
>>> # Find the top 5 routes with the biggest increases
>>> import heapq
>>> top_5_increases = heapq.nlargest(5, increases.items(), key=lambda x: x[1])
>>>
>>> # Display the results
>>> print("Top 5 routes with the greatest ridership increase from 2001 to 2011:")
>>> for route, increase in top_5_increases:
...     print(f"Route {route}: increased by {increase:,} rides")
...     print(f"  2001 rides: {rides_2001[route]:,}")
...     print(f"  2011 rides: {rides_2011[route]:,}")
...     print()
```

We first create two `Counter` objects, `rides_2001` and `rides_2011`, to store the total rides for each route in 2001 and 2011 respectively. As we iterate over each row in the `rows` list, we check if the date starts with '2001 -' or '2011 -' and add the rides to the appropriate counter.

Then, we create an empty dictionary `increases` to store the increase in ridership for each route. We iterate over the unique routes and calculate the increase by subtracting the 2001 rides from the 2011 rides for each route.

To find the top 5 routes with the biggest increases, we use the `heapq.nlargest` function. This function takes the number of elements to return (5 in this case), the iterable (`increases.items()`), and a key function (`lambda x: x[1]`) that specifies how to compare the elements.

Finally, we print the results, showing the route number, the increase in ridership, and the number of rides in 2001 and 2011.

This analysis identifies which bus routes experienced the most growth in ridership over the decade, which could indicate changing population patterns, service improvements, or other interesting trends.

You can extend these analyses in many ways. For example, you might want to:

- Analyze ridership patterns by day of the week
- Find routes with declining ridership
- Compare seasonal variations in ridership

The techniques you've learned in this lab provide a solid foundation for this kind of data exploration and analysis.
