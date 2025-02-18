# 固定オフセットボックスを作成する

AnnotationBbox を使用して固定オフセットボックスを作成し、オフセットボックスを追加してその位置を設定します。以下のコードを使用して固定オフセットボックスを作成します。

```python
ao = AnchoredOffsetbox(loc='upper left', child=offsetbox, frameon=True,
                           borderpad=0.2)
ax1.add_artist(ao)
```
