# 棒グラフを作成する

このステップでは、Matplotlib を使って棒グラフを作成します。まず、NumPy の`random()`関数を使ってプロットするデータを生成します。そして、`bar()`関数を使ってグラフを作成します。

```python
x = ['A', 'B', 'C', 'D', 'E']
y = np.random.randint(1, 10, 5)

plt.bar(x, y)
plt.show()
```
