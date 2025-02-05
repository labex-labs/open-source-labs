# 自定义箱线图

我们可以通过更改箱体、须线和异常值的外观来自定义箱线图。我们还可以在同一图表上创建多个箱线图，以比较不同的数据组。以下是一些自定义箱线图的示例：

```python
# 创建一个带缺口的箱线图
plt.boxplot(data, notch=True)
plt.show()

# 将异常值点符号更改为绿色菱形
plt.boxplot(data, flierprops=dict(marker='D', markerfacecolor='g', markersize=8))
plt.show()

# 创建水平箱线图
plt.boxplot(data, vert=False)
plt.show()

# 在一个图表上创建多个箱线图
data1 = np.random.normal(0, 1, 50)
data2 = np.random.normal(1, 1, 50)
data3 = np.random.normal(2, 1, 50)

plt.boxplot([data1, data2, data3])
plt.show()
```
