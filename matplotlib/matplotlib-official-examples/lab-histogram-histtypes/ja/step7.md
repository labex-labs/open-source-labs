# 積み重ね棒グラフで 2 つのヒストグラムを作成する

`hist`関数を 2 回呼び出し、`histtype`パラメータを`'barstacked'`に設定することで、積み重ね棒グラフで 2 つのヒストグラムを作成できます。この例では、積み重ね棒グラフで 2 つのヒストグラムを作成します。

```python
plt.hist(x, density=True, histtype='barstacked', rwidth=0.8)
plt.hist(w, density=True, histtype='barstacked', rwidth=0.8)
plt.show()
```
