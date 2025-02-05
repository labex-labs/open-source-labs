# Create Scatter Plot

In this step, we will create a scatter plot using the random data from Step 2.

```python
fig, ax = plt.subplots(figsize=(5.5, 5.5))
ax.scatter(x, y)
ax.set_aspect(1.)
```
