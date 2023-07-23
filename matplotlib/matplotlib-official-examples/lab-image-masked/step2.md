# Creating Data

Next, we will create some data to use in our plots. For this tutorial, we will create a simple line plot.

```python
# Create the data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
plt.plot(x, y)
plt.show()
```
