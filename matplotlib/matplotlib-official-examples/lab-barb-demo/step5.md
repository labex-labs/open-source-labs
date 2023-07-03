# Create Masked Wind Barb Plot

We can also create a masked wind barb plot by using a masked array. In this case, we will change the value of one vector to a bad value and mask it.

```python
masked_u = np.ma.masked_array(U)
masked_u[4] = 1000  # Bad value that should not be plotted when masked
masked_u[4] = np.ma.masked

plt.barbs(X, Y, masked_u, V, length=8, pivot='middle')
plt.show()
```
