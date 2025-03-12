# Data Analysis Challenge with Chicago Transit Authority Data

Now that you've practiced with different Python data structures and the collections module, let's apply these skills to a real-world data analysis task. We'll analyze Chicago Transit Authority (CTA) bus ridership data.

## Understanding the Data

First, let's examine the transit data we'll be working with. In your Python terminal:

```python
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('/home/labex/project/ctabus.csv')
>>> print(len(rows))
# This will show the number of records in the dataset

>>> # Let's look at the first record to understand the structure
>>> import pprint
>>> pprint.pprint(rows[0])
```

The data contains daily ridership records for different bus routes. Each record includes:

- `route`: The bus route number
- `date`: The date in format "YYYY-MM-DD"
- `daytype`: Either "W" for weekday, "A" for Saturday, or "U" for Sunday/holiday
- `rides`: The number of riders that day

## Analysis Tasks

Let's solve each of the challenge questions one by one:

### Question 1: How many bus routes exist in Chicago?

To answer this, we need to find all unique route numbers in the dataset:

```python
>>> # Get all unique route numbers using a set comprehension
>>> unique_routes = {row['route'] for row in rows}
>>> print(len(unique_routes))
```

We can also see what some of these routes are:

```python
>>> # Print a few of the route numbers
>>> print(list(unique_routes)[:10])
```

### Question 2: How many people rode the number 22 bus on February 2, 2011?

For this question, we need to filter the data to find the specific record:

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

You can modify this to check any route on any date by changing the `target_date` and `target_route` variables.

### Question 3: What is the total number of rides taken on each bus route?

Let's use a Counter to calculate the total rides per route:

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

### Question 4: What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?

This is more complex. We need to compare ridership in 2001 vs. 2011 for each route:

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

This analysis identifies which bus routes experienced the most growth in ridership over the decade, which could indicate changing population patterns, service improvements, or other interesting trends.

You can extend these analyses in many ways. For example, you might want to:

- Analyze ridership patterns by day of the week
- Find routes with declining ridership
- Compare seasonal variations in ridership

The techniques you've learned in this lab provide a solid foundation for this kind of data exploration and analysis.
