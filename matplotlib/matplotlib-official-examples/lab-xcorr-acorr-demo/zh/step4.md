# 绘制自相关

现在我们将使用 Matplotlib 中的 `acorr` 函数绘制 `x` 数组的自相关。

```python
fig, ax = plt.subplots()
ax.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
ax.grid(True)
plt.show()
```

`acorr` 函数接受以下参数：

- `x`：要计算自相关的数据数组
- `usevlines`：布尔值，是否绘制从 0 到相关值的垂直线
- `normed`：布尔值，是否对相关值进行归一化
- `maxlags`：整数，计算相关性的最大滞后数
- `lw`：整数，绘图的线宽
