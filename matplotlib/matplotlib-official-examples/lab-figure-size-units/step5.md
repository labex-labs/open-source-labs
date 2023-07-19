# Quick Interactive Work

For quick interactive work, pixels are usually a good size of unit. We can use the default dpi value of 100 to convert pixel values to inches. We can then use this value as the figsize parameter in the subplots function. The code below shows how to create a figure with a size of 6 inches x 2 inches using pixel values.

```python
plt.subplots(figsize=(600/100, 200/100))
plt.show()
```
