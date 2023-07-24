# Create the Plot

Now, we will create the plot using the `tricontourf()` function and customize the view angle.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontourf(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)

plt.show()
```
