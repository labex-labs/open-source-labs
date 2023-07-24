# Create a Simple Plot

To create a simple plot in Matplotlib, you need to provide a list of numbers that you want to plot. In this case, we will plot a list of numbers against their index resulting in a straight line. Use a format string (here, 'o-r') to set the markers (circles), linestyle (solid line) and color (red).

```python
plt.plot([1, 2, 3, 4], 'o-r')
plt.ylabel('some numbers')
plt.show()
```
