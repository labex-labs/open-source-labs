# 创建示例

最后，我们将使用自定义投影创建一个示例。

```python
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    # 现在使用自定义投影创建一个简单示例。
    fig, ax = plt.subplots(subplot_kw={'projection': 'custom_hammer'})
    ax.plot([-1, 1, 1], [-1, -1, 1], "o-")
    ax.grid()

    plt.show()
```
