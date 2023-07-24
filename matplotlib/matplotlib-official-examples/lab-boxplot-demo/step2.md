# Generate the data

Next, we will generate some sample data to use in our boxplots. For this tutorial, we will use the following data:

```python
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))
```
