# Generating the Data

Next, we will generate some fake data to use in our plot. We will create two arrays, `a` and `b`, using the NumPy `arange` function. We then calculate two more arrays, `c` and `d`, using the `exp` function to compute the exponential of `a` and `d` as the reverse of `c`.

```python
# Make some fake data.
a = b = np.arange(0, 3, .02)
c = np.exp(a)
d = c[::-1]
```
