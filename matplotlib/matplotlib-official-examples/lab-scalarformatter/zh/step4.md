# 在子图上绘制数据

我们将在步骤 3 创建的子图上绘制生成的数据。

```python
for col in axs.T:
    col[0].plot(plot1_x, plot1_y)
    col[1].plot(plot2_x, plot2_y)
    col[2].plot(plot3_x, plot3_y)
```
