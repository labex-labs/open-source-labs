# Customize the Chart

We can customize the chart further by adding axis labels and a title. We can also change the color of the axis labels and the legend title. The following code demonstrates how to customize the chart:

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply', color='blue')
ax.set_xlabel('fruit names', color='blue')
ax.set_title('Fruit supply by kind and color', color='purple')
ax.legend(title='Fruit color', title_color='red', labelcolor='green')
plt.show()
```

#
