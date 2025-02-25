# 扇形にラベルを追加する

`pie()` 関数の `labels` パラメータにラベルのリストを渡すことで、扇形にラベルを追加できます。

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
```
