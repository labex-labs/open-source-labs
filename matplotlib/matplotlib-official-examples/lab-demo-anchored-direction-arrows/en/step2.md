# Create a plot

Next, we will create a simple plot using NumPy. This plot will serve as a background for the anchored direction arrows.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.imshow(np.random.random((10, 10)))
```
