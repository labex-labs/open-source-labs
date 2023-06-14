# Generate Data

We will generate data using NumPy. We will generate 100 data points with a uniform distribution between 0 and 5. We will set the threshold to 2.5 and generate the labels using a Boolean expression. We will use the first 50 data points as training data and the remaining as test data.

```python
train_size = 50
rng = np.random.RandomState(0)
X = rng.uniform(0, 5, 100)[:, np.newaxis]
y = np.array(X[:, 0] > 2.5, dtype=int)
```


