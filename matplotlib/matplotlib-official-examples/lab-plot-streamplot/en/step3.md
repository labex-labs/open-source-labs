# Varying Density

In this step, we will create a streamplot with varying density. The `density` parameter controls the number of streamlines to be plotted. Higher values will result in more streamlines.

```python
plt.streamplot(X, Y, U, V, density=[0.5, 1])
plt.title('Varying Density')
plt.show()
```
