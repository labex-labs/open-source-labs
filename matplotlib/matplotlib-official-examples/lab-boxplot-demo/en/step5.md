# Add labels and titles

Finally, we can add labels and titles to our boxplot to make it more informative. We can add labels to the x and y axes, as well as a title to the plot. We can also change the font size and style of the labels and title. Here is an example of how to add labels and titles:

```python
plt.boxplot([data1, data2, data3])
plt.xlabel('Group')
plt.ylabel('Value')
plt.title('Comparison of Three Groups')
plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.show()
```
