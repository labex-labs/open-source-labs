# Masking Data Points and Creating Scatter Plot

We mask the data points based on their distance from the origin. Data points with a distance less than `r0` are masked in `area1`, and those with a distance greater than or equal to `r0` are masked in `area2`. We then create a scatter plot of the masked data points with `marker='^'` and `marker='o'` for `area1` and `area2`, respectively.

```python
r = np.sqrt(x ** 2 + y ** 2)
area1 = np.ma.masked_where(r < r0, area)
area2 = np.ma.masked_where(r >= r0, area)
plt.scatter(x, y, s=area1, marker='^', c=c)
plt.scatter(x, y, s=area2, marker='o', c=c)
```
