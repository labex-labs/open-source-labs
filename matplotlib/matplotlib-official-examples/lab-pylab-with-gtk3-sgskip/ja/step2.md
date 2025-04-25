# グラフと軸の作成

次に、`subplots()` メソッドを使ってグラフと軸を作成します。その後、軸に 2 つの線をプロットし、それらを区別するために凡例を追加します。

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()
```
