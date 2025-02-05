# 绘制数据

我们将使用 `plot()` 函数两次绘制在步骤 2 中生成的随机数据。第一次绘制的透明度值为 0.2，第二次绘制的透明度值为 1.0，并将裁剪路径设置为黄色圆形补丁。

```python
ax.plot(x, y, alpha=0.2)
line, = ax.plot(x, y, alpha=1.0, clip_path=circ)
ax.set_title("Left click and drag to move looking glass")
```
