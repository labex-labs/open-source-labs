# Create Data for the Line Plot

In this step, we will create data for our line plot. We will use NumPy's `linspace` function to create an array of evenly spaced values between 0 and 10. We will also generate some random noise using NumPy's `random.randn` function.

```python
x = np.linspace(0, 10)
np.random.seed(19680801)
noise = np.random.randn(50)
```
