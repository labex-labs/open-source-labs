# Generating Data

We will generate some sample data to apply our penalties on. For this example, we will generate two classes of data with 100 samples each.

```python
np.random.seed(42)

# Generate two classes of data
X = np.random.randn(200, 2)
y = np.repeat([1, -1], 100)
```
