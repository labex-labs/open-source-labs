# Preparing the data

We start by preparing dummy data with a sinusoidal relationship and some Gaussian noise. We use Numpy's `linspace()` function to create a 1D array of 100 evenly spaced values between 0 and 6. We then use the `np.newaxis` attribute to convert the 1D array to a 2D array of shape `(100,1)`. We apply the `sin()` function to this array and add a second sine wave obtained by multiplying the array by 6. We then add some Gaussian noise with a mean of 0 and standard deviation of 0.1 using Numpy's `normal()` function.

```python
import numpy as np

rng = np.random.RandomState(1)
X = np.linspace(0, 6, 100)[:, np.newaxis]
y = np.sin(X).ravel() + np.sin(6 * X).ravel() + rng.normal(0, 0.1, X.shape[0])
```
