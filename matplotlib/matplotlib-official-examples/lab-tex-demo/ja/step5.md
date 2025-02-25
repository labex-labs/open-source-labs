# 棒グラフを作成する

このステップでは、Matplotlibを使って棒グラフを作成します。まず、NumPyの`random()`関数を使ってプロットするデータを生成します。そして、`bar()`関数を使ってグラフを作成します。

```python
x = ['A', 'B', 'C', 'D', 'E']
y = np.random.randint(1, 10, 5)

plt.bar(x, y)
plt.show()
```
