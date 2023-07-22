# Create the First Plot

Now, let's create the first plot using `subplot`. `subplot` takes three arguments: the number of rows, the number of columns, and the plot number. In this example, we will create a plot with 2 rows and 1 column (`211`), which means the first plot will be in the top row.

```python
ax1 = plt.subplot(211)
ax1.plot(t, np.sin(2*np.pi*t))
```
