# Modify the Shadow

We can modify the shadow of the pie chart by passing a dictionary of arguments to the `shadow` parameter of the `pie()` function.

```python
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow={'ox': -0.04, 'edgecolor': 'none', 'shade': 0.9}, startangle=90)
```
