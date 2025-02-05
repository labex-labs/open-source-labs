# Create data for plotting

Next, we need to create some data to plot. In this lab, we will be using the sine function to create our data. We will generate 500 evenly spaced points between 0 and 10 and calculate the sine of each point using the `np.sin()` function.

```python
x = np.linspace(0, 10, 500)
y = np.sin(x)
```
