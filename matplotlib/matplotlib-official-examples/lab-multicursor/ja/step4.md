# マルチカーソルの追加

最後に、データポイントの上にマウスを置いたときに、すべての3つのプロットにカーソルを表示するために `MultiCursor` 関数を追加します。

```python
multi = MultiCursor(None, (ax1, ax2, ax3), color='r', lw=1)
plt.show()
```
