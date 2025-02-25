# データを定義する

このステップでは、3Dのステムプロットを作成するために使用するデータを定義します。角度用のlinspace配列を作成し、正弦と余弦関数を使ってx座標とy座標を計算します。また、z座標を角度として定義します。

```python
theta = np.linspace(0, 2*np.pi)
x = np.cos(theta - np.pi/2)
y = np.sin(theta - np.pi/2)
z = theta
```
