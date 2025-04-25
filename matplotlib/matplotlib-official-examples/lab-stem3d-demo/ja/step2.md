# データを定義する

このステップでは、3D のステムプロットを作成するために使用するデータを定義します。角度用の linspace 配列を作成し、正弦と余弦関数を使って x 座標と y 座標を計算します。また、z 座標を角度として定義します。

```python
theta = np.linspace(0, 2*np.pi)
x = np.cos(theta - np.pi/2)
y = np.sin(theta - np.pi/2)
z = theta
```
