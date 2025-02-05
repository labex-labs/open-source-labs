# Generate the Data

We will be using the linspace method from the Numpy library to generate the data for the animation. We will be generating two sets of data, x and y, and then reshaping the y data to create a two-dimensional array.

```python
x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
```
