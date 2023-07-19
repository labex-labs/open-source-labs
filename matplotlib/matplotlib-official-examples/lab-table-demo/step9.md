# Add Axis Labels and Title

We will add axis labels and a title to the plot using the `plt.ylabel`, `plt.yticks`, `plt.xticks`, and `plt.title` functions.

```python
values = np.arange(0, 2500, 500)
value_increment = 1000

plt.ylabel(f"Loss in ${value_increment}'s")
plt.yticks(values * value_increment, ['%d' % val for val in values])
plt.xticks([])
plt.title('Loss by Disaster')
```
