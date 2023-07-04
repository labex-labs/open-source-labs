# Customize the plot appearance

We can further customize the appearance of our plot. Follow these steps:

1. Rotate the x-axis labels to make them more readable.

```python
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
```

2. Set the x-axis and y-axis limits, labels, and title.

```python
ax.set(xlim=[-10000, 140000],
       xlabel='Total Revenue',
       ylabel='Company',
       title='Company Revenue')
```

3. Show the plot again.

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
```
