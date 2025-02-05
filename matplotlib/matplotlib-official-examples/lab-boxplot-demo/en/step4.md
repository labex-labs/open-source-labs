# Customize the boxplot

We can customize the boxplot by changing the appearance of the box, whiskers, and outliers. We can also create multiple boxplots on the same plot to compare different groups of data. Here are some examples of how to customize the boxplot:

```python
# Create a notched boxplot
plt.boxplot(data, notch=True)
plt.show()

# Change the outlier point symbols to green diamonds
plt.boxplot(data, flierprops=dict(marker='D', markerfacecolor='g', markersize=8))
plt.show()

# Create horizontal boxplots
plt.boxplot(data, vert=False)
plt.show()

# Create multiple boxplots on one plot
data1 = np.random.normal(0, 1, 50)
data2 = np.random.normal(1, 1, 50)
data3 = np.random.normal(2, 1, 50)

plt.boxplot([data1, data2, data3])
plt.show()
```
