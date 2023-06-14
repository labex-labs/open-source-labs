# Unbroken Streamlines

In this step, we will create a streamplot with unbroken streamlines. The `broken_streamlines` parameter controls whether the streamlines should be broken when they exceed the limit of lines within a single grid cell.

```python
plt.streamplot(X, Y, U, V, broken_streamlines=False)
plt.title('Streamplot with Unbroken Streamlines')
plt.show()
```
