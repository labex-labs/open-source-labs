# プロットに楕円を追加する

このステップでは、プロットに楕円を追加します。楕円を作成するには `Ellipse` 関数を使い、位置、幅、高さ、角度などの楕円のプロパティをカスタマイズします。

```python
ax = axs.flat[1]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
```
