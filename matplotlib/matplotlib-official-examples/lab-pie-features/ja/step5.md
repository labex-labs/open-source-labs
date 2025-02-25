# 色をカスタマイズする

`pie()` 関数の `colors` パラメータに色のリストを渡すことで、扇形の色をカスタマイズできます。

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=['olivedrab', 'rosybrown', 'gray','saddlebrown'])
```
