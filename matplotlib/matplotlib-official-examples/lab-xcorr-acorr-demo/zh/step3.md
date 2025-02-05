# 绘制互相关

现在我们将使用 Matplotlib 中的 `xcorr` 函数绘制这两个数组之间的互相关。

```python
fig, ax = plt.subplots()
ax.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
ax.grid(True)
plt.show()
```

`xcorr` 函数接受以下参数：

- `x`：第一个数据数组
- `y`：第二个数据数组
- `usevlines`：布尔值，是否绘制从 0 到相关值的垂直线
- `maxlags`：整数，计算相关性的最大滞后数
- `normed`：布尔值，是否对相关值进行归一化
- `lw`：整数，绘图的线宽
