# 可视化结果

我们将绘制数据以及线性模型和 RANSAC 回归器的拟合线。

```python
# 可视化结果
lw = 2
plt.scatter(
    X[内点掩码], y[内点掩码], color="yellowgreen", marker=".", label="内点"
)
plt.scatter(
    X[外点掩码], y[外点掩码], color="gold", marker=".", label="外点"
)
plt.plot(line_X, line_y, color="navy", linewidth=lw, label="线性回归器")
plt.plot(
    line_X,
    line_y_ransac,
    color="cornflowerblue",
    linewidth=lw,
    label="RANSAC 回归器"
)
plt.legend(loc="lower right")
plt.xlabel("输入")
plt.ylabel("响应")
plt.show()
```
