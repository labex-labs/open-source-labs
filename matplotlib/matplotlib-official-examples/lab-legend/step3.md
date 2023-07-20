# Creating the Plot

Now we are ready to create our plot. We will use the `plot` function of Matplotlib to plot three lines on the same graph, each with a pre-defined label. We will use the `label` parameter to assign the labels to each line.

```python
# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(a, c, 'k--', label='Model length')
ax.plot(a, d, 'k:', label='Data length')
ax.plot(a, c + d, 'k', label='Total message length')
```
