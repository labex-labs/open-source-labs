# Create Some Mock Data

Next, we will create some mock data to use for our plots. We will be using `numpy.arange` to create an array of values ranging from 0.01 to 10.0 with a step of 0.01. We will then use `numpy.exp` and `numpy.sin` to create two sets of data.

```python
# Create some mock data
t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)
data2 = np.sin(2 * np.pi * t)
```
