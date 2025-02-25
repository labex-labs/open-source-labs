# 楕円用のデータを作成する

x座標、y座標、幅、高さ、角度の配列の形式で、楕円用のデータを作成します。

```python
x = np.arange(10)
y = np.arange(15)
X, Y = np.meshgrid(x, y)

XY = np.column_stack((X.ravel(), Y.ravel()))

ww = X / 10.0
hh = Y / 15.0
aa = X * 9
```
