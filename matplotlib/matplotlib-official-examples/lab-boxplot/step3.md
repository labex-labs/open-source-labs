# Default Box Plot

We will start by creating a default box plot to visualize the data. We will use the Matplotlib function `boxplot()` and pass the data and labels as arguments. We will also set the title of the plot using the `set_title()` function.

```python
fig, ax = plt.subplots()
ax.boxplot(data, labels=labels)
ax.set_title('Default Box Plot')
plt.show()
```
