# Plot the Samples

We will plot the samples using the `scatter` function from `matplotlib.pyplot`.

```python
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, edgecolors="k")
```


