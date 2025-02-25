# サイズを制御する

`pie()` 関数の `radius` パラメータを設定することで、円グラフのサイズを制御できます。

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%.0f%%',
       textprops={'size':'smaller'}, radius=0.5)
```
