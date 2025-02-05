# Varying Color

In this step, we will create a streamplot with varying color. The `color` parameter takes a 2D array that represents the magnitude of the vector field. Here, we are using the `U` component of the vector field as the color.

```python
strm = plt.streamplot(X, Y, U, V, color=U, linewidth=2, cmap='autumn')
plt.colorbar(strm.lines)
plt.title('Varying Color')
plt.show()
```
