# Creating Multiple Plots

We can also create multiple plots in the same figure.

```python
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title('Plot 1')

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title('Plot 2')

plt.show()
```

Here, we are using the `subplot` function to create two plots side-by-side in the same figure. We pass three arguments to `subplot`: the number of rows, the number of columns, and the plot number. We then create a plot in each subplot.
