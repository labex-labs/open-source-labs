# 積み重ね棒グラフで2つのヒストグラムを作成する

`hist`関数を2回呼び出し、`histtype`パラメータを`'barstacked'`に設定することで、積み重ね棒グラフで2つのヒストグラムを作成できます。この例では、積み重ね棒グラフで2つのヒストグラムを作成します。

```python
plt.hist(x, density=True, histtype='barstacked', rwidth=0.8)
plt.hist(w, density=True, histtype='barstacked', rwidth=0.8)
plt.show()
```
