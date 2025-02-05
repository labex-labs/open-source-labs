# Create the subplots

We will create a figure with two subplots using `.pyplot.subplot`.

```python
plt.figure()

plt.subplot(211)
plt.plot(t1, f(t1), color='tab:blue', marker='o')
plt.plot(t2, f(t2), color='black')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), color='tab:orange', linestyle='--')

plt.show()
```

The `subplot()` function takes three arguments: the number of rows, the number of columns, and the index of the current plot. The index starts from 1 in the upper left corner and increases row-wise. In this example, we create a figure with two subplots: one on top and one on the bottom.

In the first subplot, we plot `t1` against `f(t1)` and `t2` against `f(t2)`. We set the color of the first plot to blue and add circular markers to each data point. We set the color of the second plot to black.

In the second subplot, we plot `t2` against the cosine function of `2*np.pi*t2`. We set the color of the plot to orange and the linestyle to dashed.
