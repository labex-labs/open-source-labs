# 単純な折れ線グラフを作成する

このステップでは、Matplotlib を使って単純な折れ線グラフを作成します。まず、NumPy の`linspace()`関数と`cos()`関数を使ってプロットするデータを生成します。そして、`plot()`関数を使ってグラフを作成します。

```python
t = np.linspace(0.0, 1.0, 100)
s = np.cos(4 * np.pi * t) + 2

plt.plot(t, s)
plt.show()
```
