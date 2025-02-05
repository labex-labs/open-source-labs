# Customize the Z Axis

```python
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')
```

We customize the z axis using the `set_zlim()` function to set the limits of the z axis to -1.01 to 1.01. We then use the `set_major_locator()` function to set the number of ticks on the z axis to 10 using `LinearLocator(10)`. Finally, we use the `set_major_formatter()` function to format the z axis tick labels using a `StrMethodFormatter`.
