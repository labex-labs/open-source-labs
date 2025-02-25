# 乱数データを生成する

このステップでは、散布図用の乱数データを生成します。NumPyライブラリを使って、各変数について50個のデータポイントを生成します。

```python
np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
```
