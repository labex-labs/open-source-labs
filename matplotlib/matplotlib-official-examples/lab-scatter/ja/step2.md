# 乱数データを生成する

このステップでは、散布図用の乱数データを生成します。NumPy ライブラリを使って、各変数について 50 個のデータポイントを生成します。

```python
np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
```
