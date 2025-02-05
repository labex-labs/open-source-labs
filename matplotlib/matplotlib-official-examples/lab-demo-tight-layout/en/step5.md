# Saving the Plot

Once we have created a plot, we can save it to a file.

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title('My Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.savefig('my_plot.png')
```

Here, we are using the `savefig` function to save our plot to a file named `my_plot.png`.
