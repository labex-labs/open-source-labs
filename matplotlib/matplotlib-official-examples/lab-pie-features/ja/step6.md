# ハッチパターンをカスタマイズする

`pie()` 関数の `hatch` パラメータにハッチパターンのリストを渡すことで、扇形のハッチパターンをカスタマイズできます。

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, hatch=['**O', 'oO', 'O.O', '.||.'])
```
