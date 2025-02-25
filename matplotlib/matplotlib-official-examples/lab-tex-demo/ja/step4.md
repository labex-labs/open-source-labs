# 散布図を作成する

このステップでは、Matplotlibを使って散布図を作成します。まず、NumPyの`random()`関数を使ってプロットするランダムなデータを生成します。そして、`scatter()`関数を使ってグラフを作成します。

```python
x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y)
plt.show()
```
