# カスタムスケールを使用する

これで、プロットでカスタムスケールを使用できるようになりました。ここでは、メルカトル投影における緯度データにカスタムスケールを使用する例を示します。

```python
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    t = np.arange(-180.0, 180.0, 0.1)
    s = np.radians(t)/2.

    plt.plot(t, s, '-', lw=2)
    plt.yscale('mercator')

    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Mercator projection')
    plt.grid(True)

    plt.show()
```
