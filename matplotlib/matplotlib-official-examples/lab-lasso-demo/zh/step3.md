# 创建绘图

现在，使用 `LassoManager` 类创建一个交互式绘图。`np.random.rand` 函数生成将被绘制的随机数据点。

```python
if __name__ == '__main__':
    np.random.seed(19680801)
    ax = plt.figure().add_subplot(
        xlim=(0, 1), ylim=(0, 1), title='Lasso points using left mouse button')
    manager = LassoManager(ax, np.random.rand(100, 2))
    plt.show()
```
