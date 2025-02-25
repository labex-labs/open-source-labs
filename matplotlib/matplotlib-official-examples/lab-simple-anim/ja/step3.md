# データの生成

このステップでは、折れ線グラフ用のデータを生成します。x軸の値の配列を生成するためにNumPyの`arange()`関数を、サイン波のy軸の値の配列を生成するために`sin()`関数を使用します。

```python
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))
```
