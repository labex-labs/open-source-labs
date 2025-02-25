# サンプルの作成

最後に、カスタム投影を使用したサンプルを作成します。

```python
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    # ここでは、カスタム投影を使用した簡単なサンプルを作成します。
    fig, ax = plt.subplots(subplot_kw={'projection': 'custom_hammer'})
    ax.plot([-1, 1, 1], [-1, -1, 1], "o-")
    ax.grid()

    plt.show()
```
