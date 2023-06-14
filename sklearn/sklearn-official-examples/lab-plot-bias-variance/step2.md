# Set the Parameters

We need to set the parameters that control the size of the datasets, the number of iterations, and the standard deviation of the noise.

```python
n_repeat = 50  # Number of iterations for computing expectations
n_train = 50  # Size of the training set
n_test = 1000  # Size of the test set
noise = 0.1  # Standard deviation of the noise
np.random.seed(0)
```


