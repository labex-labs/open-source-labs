# 绘制数据

现在我们可以使用 `plot` 函数来绘制数据了。我们将使用在步骤3中创建的数据创建两条线。

```python
ax.plot(theta, r, color="tab:orange", lw=3, label="a line")
ax.plot(0.5 * theta, r, color="tab:blue", ls="--", lw=3, label="another line")
```
