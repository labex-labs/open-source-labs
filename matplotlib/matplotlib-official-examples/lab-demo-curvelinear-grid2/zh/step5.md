# 创建图形

最后一步是使用 `plt.figure` 函数创建图形。我们将把图形大小设置为(7, 4)，并调用在步骤2 - 4中创建的 `curvelinear_test1` 函数。

```python
if __name__ == "__main__":
    fig = plt.figure(figsize=(7, 4))
    curvelinear_test1(fig)
    plt.show()
```
