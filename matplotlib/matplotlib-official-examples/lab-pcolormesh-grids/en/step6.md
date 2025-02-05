# Auto Shading

It's possible that the user would like the code to automatically choose which to use, in this case, `shading='auto'` will decide whether to use `flat` or `nearest` shading based on the shapes of `X`, `Y`, and `Z`. We can visualize the grid using the following code block:

```python
fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z, shading='auto', cmap='viridis')
ax.set_title('Auto Shading')
plt.show()
```
