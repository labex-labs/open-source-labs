# Control the Size

We can control the size of the pie chart by setting the `radius` parameter of the `pie()` function.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%.0f%%',
       textprops={'size': 'smaller'}, radius=0.5)
```
