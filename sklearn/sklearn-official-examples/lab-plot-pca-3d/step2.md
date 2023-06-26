# Create Data

We will generate a random dataset for this lab. The dataset will have three variables `x`, `y`, and `z`. We will define `x` and `y` as normally distributed random variables with mean 0 and standard deviation of 0.5. `z` is also normally distributed with mean 0 and standard deviation of 0.1.

```python
e = np.exp(1)
np.random.seed(4)

y = np.random.normal(scale=0.5, size=(30000))
x = np.random.normal(scale=0.5, size=(30000))
z = np.random.normal(scale=0.1, size=len(x))
```
