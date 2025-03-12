# Enhancing the Custom Container for Slicing

Our custom container is great for accessing individual records. However, there's an issue when it comes to slicing. When you attempt to take a slice of our container, the result isn't what you'd typically expect.

Let's understand why this happens. In Python, slicing is a common operation used to extract a portion of a sequence. But for our custom container, Python doesn't know how to create a new `RideData` object with just the sliced data. Instead, it creates a list containing the results of calling `__getitem__` for each index in the slice.

1. Let's test slicing in the Python shell:

```python
import readrides

rows = readrides.read_rides_as_dicts('ctabus.csv')
r = rows[0:10]  # Take a slice of the first 10 records
type(r)  # This will likely be a list, not a RideData object
print(r)  # This might look like a list of numbers, not dictionaries
```

In this code, we first import the `readrides` module. Then we read the data from the `ctabus.csv` file into a variable `rows`. When we try to take a slice of the first 10 records and check the type of the result, we find that it's a list instead of a `RideData` object. Printing the result might show something unexpected, like a list of numbers instead of dictionaries.

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

In this updated `__getitem__` method, we first check if the `index` is a slice. If it is, we create a new `RideData` object called `result`. Then we populate this new object with slices of the original data columns (`routes`, `dates`, `daytypes`, and `numrides`). This ensures that when we slice our custom container, we get another `RideData` object instead of a list. If the `index` is not a slice (i.e., it's a single index), we return a dictionary containing the relevant record.

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

After updating the `__getitem__` method, we can test the slicing again. When we take a slice of the first 10 records, the type of the result should now be `readrides.RideData`. The length of the slice should be 10, and accessing individual elements in the slice should give us the same results as accessing the corresponding elements in the original container.

4. You can also test with different slice patterns:

```python
# Get every other record from the first 20
r2 = rows[0:20:2]
len(r2)  # Should be 10

# Get the last 10 records
r3 = rows[-10:]
len(r3)  # Should be 10
```

Here, we're testing different slice patterns. The first slice `rows[0:20:2]` gets every other record from the first 20 records, and the length of the resulting slice should be 10. The second slice `rows[-10:]` gets the last 10 records, and its length should also be 10.

By properly implementing slicing, our custom container now behaves even more like a standard Python list, while maintaining the memory efficiency of column-oriented storage.

This approach of creating custom container classes that mimic built-in Python containers but with different internal representations is a powerful technique for optimizing memory usage without changing the interface that your code presents to users.
