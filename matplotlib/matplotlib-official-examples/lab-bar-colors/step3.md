# Create the Bar Chart

Now, we can create the bar chart using the data that we defined in Step 2. We will use the `bar()` method of Matplotlib's `pyplot` module to create the chart. We will also pass in the `label` and `color` parameters to control the legend entries and the bar colors, respectively. The following code demonstrates how to create the bar chart:

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')
plt.show()
```

#
