# プロットのフォーマット

プロットをより読みやすくするために、Matplotlib のフォーマット関数を使ってフォーマットを設定できます。この例では、y 軸のラベルを数百万の値として表示するようにフォーマットします。

```python
def millions(x):
    return '$%1.1fM' % (x * 1e-6)

ax.fmt_ydata = millions
```
