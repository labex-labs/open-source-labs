# グラフにテーブルを追加する

`plt.table`関数を使って、グラフの下部にテーブルを追加します。セルのテキスト、行ラベル、行の色、列ラベルをパラメータとして関数に渡します。

```python
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')
```
