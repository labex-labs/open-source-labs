# Creating the Plot

We will create the plot and add the `PathPatch` to the plot. We will set the title of the plot to `'A Compound Path'`.

```python
fig, ax = plt.subplots()
ax.add_patch(pathpatch)
ax.set_title('A Compound Path')

ax.autoscale_view()

plt.show()
```
