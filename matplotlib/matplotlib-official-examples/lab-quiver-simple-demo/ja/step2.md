# データの作成

`np.meshgrid()` 関数を使って `X` と `Y` 座標を作成する必要があります。その後、ベクトル場を表す `U` と `V` 配列を作成します。

```python
X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)
```
