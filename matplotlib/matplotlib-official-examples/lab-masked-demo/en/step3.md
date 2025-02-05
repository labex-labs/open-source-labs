# Remove Points

We will remove points where y > 0.7. We will create a new x array and y array with only the remaining points.

```python
x2 = x[y <= 0.7]
y2 = y[y <= 0.7]
```
