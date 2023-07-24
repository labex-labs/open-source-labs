# Generate some sample data

Next, we will generate some sample data to perform density estimation on. For the purpose of this lab, let's generate a 1-dimensional dataset with 100 points. We will use a normal distribution to generate the data.

```python
np.random.seed(0)
X = np.random.normal(0, 1, 100).reshape(-1, 1)
```
