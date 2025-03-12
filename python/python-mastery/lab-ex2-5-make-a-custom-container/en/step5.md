# Enhancing the Custom Container for Slicing

Our custom container works well for accessing individual records, but there's a problem with slicing. When you try to take a slice of our container, it doesn't return what you would expect.

1. Let's test slicing in the Python shell:

```python
import readrides

rows = readrides.read_rides_as_dicts('ctabus.csv')
r = rows[0:10]  # Take a slice of the first 10 records
type(r)  # This will likely be a list, not a RideData object
print(r)  # This might look like a list of numbers, not dictionaries
```

When we slice our custom container, Python doesn't know how to create a new RideData object with just the sliced data. Instead, it creates a list containing the results of calling `__getitem__` for each index in the slice.

2. Let's modify our `RideData` class to handle slicing properly. Open `readrides.py` and update the `__getitem__` method:

```python
def __getitem__(self, index):
    if isinstance(index, slice):
        # Handle slice
        result = RideData()
        result.routes = self.routes[index]
        result.dates = self.dates[index]
        result.daytypes = self.daytypes[index]
        result.numrides = self.numrides[index]
        return result
    else:
        # Handle single index
        return {'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]}
```

This updated method checks if the index is a slice. If it is, it creates a new `RideData` object and populates it with slices of the original data columns. This ensures that slicing returns another `RideData` object rather than a list.

3. Let's test our improved slicing capability:

```python
import readrides

rows = readrides.read_rides_as_dicts('ctabus.csv')
r = rows[0:10]  # Take a slice of the first 10 records
type(r)  # Should now be readrides.RideData
len(r)   # Should be 10
r[0]     # Should be the same as rows[0]
r[1]     # Should be the same as rows[1]
```

Now when we take a slice of our custom container, we get another custom container that contains only the sliced data. This behaves much more like a regular list, which is what users of our container would expect.

4. You can also test with different slice patterns:

```python
# Get every other record from the first 20
r2 = rows[0:20:2]
len(r2)  # Should be 10

# Get the last 10 records
r3 = rows[-10:]
len(r3)  # Should be 10
```

By properly implementing slicing, our custom container now behaves even more like a standard Python list, while maintaining the memory efficiency of column-oriented storage.

This approach of creating custom container classes that mimic built-in Python containers but with different internal representations is a powerful technique for optimizing memory usage without changing the interface that your code presents to users.
