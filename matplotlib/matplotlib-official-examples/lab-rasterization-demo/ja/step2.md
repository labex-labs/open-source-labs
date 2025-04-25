# データの作成

ラスタライズの概念を説明するために使用するデータを作成します。

```python
d = np.arange(100).reshape(10, 10)  # カラーマッピングする値
x, y = np.meshgrid(np.arange(11), np.arange(11))

theta = 0.25*np.pi
xx = x*np.cos(theta) - y*np.sin(theta)  # x を-θだけ回転
yy = x*np.sin(theta) + y*np.cos(theta)  # y を-θだけ回転
```
