# Explode the Slices

We can explode one or more slices of the pie chart by passing a list of values to the `explode` parameter of the `pie()` function.

```python
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=True, startangle=90)
```
