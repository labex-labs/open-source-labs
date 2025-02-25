# 影を変更する

`pie()` 関数の `shadow` パラメータに引数の辞書を渡すことで、円グラフの影を変更できます。

```python
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow={'ox': -0.04, 'edgecolor': 'none','shade': 0.9}, startangle=90)
```
