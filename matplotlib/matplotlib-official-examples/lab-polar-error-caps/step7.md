# Create Large Radius Error Bars

In this step, we will create large radius error bars to demonstrate how they can lead to unwanted scale in the data, reducing the displayed range.

```python
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='polar')
ax.errorbar(theta, r, xerr=0.25, yerr=10.1, capsize=7, fmt="o", c="orangered")
ax.set_title("Large Radius Error Bars")
plt.show()
```
