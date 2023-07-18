# Create the Quiver Plot

We can create the quiver plot using the `ax.quiver()` function. We pass in the `X`, `Y`, `U`, and `V` arrays as parameters.

```python
fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V)
```
