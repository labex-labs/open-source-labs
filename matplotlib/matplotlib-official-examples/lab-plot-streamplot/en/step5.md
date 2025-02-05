# Varying Line Width

In this step, we will create a streamplot with varying line width. The `linewidth` parameter controls the width of the streamlines. Here, we are using the `speed` array that we calculated earlier to vary the linewidth.

```python
lw = 5*speed / speed.max()
plt.streamplot(X, Y, U, V, density=0.6, color='k', linewidth=lw)
plt.title('Varying Line Width')
plt.show()
```
