# Y 軸の範囲を設定する

最初のサブプロットの y 軸を制限して外れ値（outlier）のみを表示し、2 番目のサブプロットの y 軸を制限して大部分のデータを表示します。`ax1.set_ylim` と `ax2.set_ylim` を使用して y 軸の範囲を設定します。

```python
ax1.set_ylim(.78, 1.)  # outliers only
ax2.set_ylim(0,.22)  # most of the data
```
