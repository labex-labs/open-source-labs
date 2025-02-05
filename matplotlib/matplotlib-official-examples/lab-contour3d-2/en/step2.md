# Create Data

Next, we need to create the data we will use to generate the contour plot. We will use the `get_test_data()` function from the `mpl_toolkits.mplot3d` module to generate sample data.

```python
X, Y, Z = axes3d.get_test_data(0.05)
```
