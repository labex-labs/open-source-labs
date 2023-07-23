# Create a Simple Contour Plot with Labels

Now that we have our data, we can create a simple contour plot with labels using default colors.

```python
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Simplest default with labels')
```
