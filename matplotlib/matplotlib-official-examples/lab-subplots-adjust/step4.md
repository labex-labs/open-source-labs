# Adjust Colorbar Position

We can also adjust the position of the color bar using `plt.axes`. This function takes a list of `[left, bottom, width, height]` values as arguments to specify the position and size of the axes. Run the following code:

```python
cax = plt.axes([0.85, 0.1, 0.075, 0.8])
plt.colorbar(cax=cax)
```
