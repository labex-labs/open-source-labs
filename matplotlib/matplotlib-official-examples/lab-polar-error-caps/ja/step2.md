# データを作成する

このステップでは、誤差棒プロット用のデータを作成します。NumPyを使って、theta値の配列と対応する半径値の配列を作成します。

```python
theta = np.arange(0, 2 * np.pi, np.pi / 4)
r = theta / np.pi / 2 + 0.5
```
