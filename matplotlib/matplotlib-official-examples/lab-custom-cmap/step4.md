# Use the Custom Colormap

We can use the custom colormap in our visualizations by passing the name of the colormap to the `cmap` parameter of Matplotlib's plotting functions.

```python
# create some data
x = np.arange(0, np.pi, 0.1)
y = np.arange(0, 2 * np.pi, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.cos(X) * np.sin(Y) * 10

# plot the data using the custom colormap
plt.imshow(Z, cmap='BlueRed')
plt.colorbar()
plt.show()
```
