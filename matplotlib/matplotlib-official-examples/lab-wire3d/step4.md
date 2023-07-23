# Customize the Plot

We can customize the plot to make it more visually appealing. In this example, we will add a title, axis labels, and change the color of the plot.

```python
# Customize the plot
ax.set_title('Wireframe Plot')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5, color='green')
```
