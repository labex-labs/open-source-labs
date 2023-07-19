# Generate a Filled Polygon

Now, we can generate a filled polygon using the `fill()` function. We will use the Koch snowflake function to generate the coordinates for the polygon.

```python
x, y = koch_snowflake(order=5)

plt.figure(figsize=(8, 8))
plt.axis('equal')
plt.fill(x, y)
plt.show()
```
