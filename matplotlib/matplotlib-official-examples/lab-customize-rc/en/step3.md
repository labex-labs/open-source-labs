# Create Subplots

To create subplots in Matplotlib, you can use the `subplot()` method. This method takes three arguments: the number of rows, the number of columns, and the plot number. Here's an example that creates three subplots:

```python
plt.subplot(311)
plt.plot([1, 2, 3])

plt.subplot(312)
plt.plot([1, 2, 3])
plt.grid(True)

plt.subplot(313)
plt.plot([1, 2, 3])
plt.grid(True)
```
