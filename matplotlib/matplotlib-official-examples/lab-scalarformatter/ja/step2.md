# 例としてのグラフ用のデータを生成する

`~.axes.Axes.ticklabel_format`を使ったさまざまな設定を示すために、3つのグラフ用のデータを生成します。

```python
x = np.arange(0, 1,.01)

# Plot 1
plot1_x = x * 1e5 + 1e10
plot1_y = x * 1e-10 + 1e-5

# Plot 2
plot2_x = x * 1e5
plot2_y = x * 1e-4

# Plot 3
plot3_x = -x * 1e5 - 1e10
plot3_y = -x * 1e-5 - 1e-10
```
