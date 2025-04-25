# 扇形を分離する

`pie()` 関数の `explode` パラメータに値のリストを渡すことで、円グラフの 1 つまたは複数の扇形を分離できます。

```python
explode = (0, 0.1, 0, 0)  # 2 番目の扇形（すなわち 'Hogs'）のみを「分離」する

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=True, startangle=90)
```
