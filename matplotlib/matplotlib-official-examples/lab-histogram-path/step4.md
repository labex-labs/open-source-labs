# Generate the corners of the rectangles

In order to draw our histogram using rectangles, we need to calculate the corners of each rectangle. Add the following code:

```python
left = bins[:-1]
right = bins[1:]
bottom = np.zeros(len(left))
top = bottom + n
```
