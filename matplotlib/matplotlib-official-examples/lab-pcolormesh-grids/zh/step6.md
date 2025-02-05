# 自动着色

用户可能希望代码自动选择使用哪种方式，在这种情况下，`shading='auto'` 将根据 `X`、`Y` 和 `Z` 的形状决定使用 `flat` 还是 `nearest` 着色。我们可以使用以下代码块来可视化该网格：

```python
fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z, shading='auto', cmap='viridis')
ax.set_title('Auto Shading')
plt.show()
```
