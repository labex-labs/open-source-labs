# 绘制变量及对称误差线

现在我们将绘制带有可变对称误差线的数据。`ax.errorbar()`函数用于创建绘图，`yerr`参数用于指定误差值。

```python
# 绘制变量及对称误差线
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=error, fmt='-o')
ax.set_title('Variable, Symmetric Error Bars')
plt.show()
```
