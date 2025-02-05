# 创建条形图

现在我们准备好创建条形图了。我们将首先定义一些变量，这些变量将帮助我们设置条形的宽度及其在x轴上的位置。

```python
dim = len(data[0])
w = 0.75
dimw = w / dim
```

接下来，我们将使用`subplots()`方法创建一个图形和一个轴对象。然后，我们将使用for循环遍历数据集中的每个值，并为每个值创建一个条形。

```python
fig, ax = plt.subplots()
x = np.arange(len(data))
for i in range(len(data[0])):
    y = [d[i] for d in data]
    b = ax.bar(x + i * dimw, y, dimw, bottom=0.001)
```

我们将`bottom`参数设置为`0.001`，以避免出现高度为0的条形，因为这与对数刻度不兼容。
