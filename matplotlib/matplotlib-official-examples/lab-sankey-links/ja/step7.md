# 最初の図を追加する

`flows=[1, -1]` と `orientations=[0, 1]` を使って `sankey.add()` を使って最初の図を追加します。

```python
sankey.add(flows=[1, -1], orientations=[0, 1],
           patchlabel="0", facecolor='k',
           rotation=45)
```
