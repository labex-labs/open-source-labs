# 创建等高线图

现在我们将使用 `contourf()` 方法创建等高线图。此方法创建填充等高线。我们将把 `cmap` 参数设置为 `cm.coolwarm` 以使用冷色-暖色颜色映射。

```python
ax.contourf(X, Y, Z, cmap=cm.coolwarm)
```
