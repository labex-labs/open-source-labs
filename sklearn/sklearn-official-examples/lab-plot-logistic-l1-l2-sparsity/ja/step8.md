# タイトルとラベルを設定する

サブプロットのタイトルとラベルを設定します。

```python
    if i == 0:
        axes_row[0].set_title("L1 ペナルティ")
        axes_row[1].set_title("エラスティックネット\nl1_ratio = %s" % l1_ratio)
        axes_row[2].set_title("L2 ペナルティ")

    axes_row[0].set_ylabel("C = %s" % C)
```
