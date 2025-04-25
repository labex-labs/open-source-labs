# 生成辛顿图

现在，我们将使用 numpy 生成一个随机权重矩阵，然后使用 `hinton` 函数生成辛顿图。

```python
if __name__ == '__main__':
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    hinton(np.random.rand(20, 20) - 0.5)
    plt.show()
```
