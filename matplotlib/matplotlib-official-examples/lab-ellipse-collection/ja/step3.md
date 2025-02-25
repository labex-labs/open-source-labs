# 楕円コレクションを作成する

上記のデータを使って`EllipseCollection`を作成し、単位を'x'と指定し、オフセットを`XY`とします。

```python
fig, ax = plt.subplots()

ec = EllipseCollection(ww, hh, aa, units='x', offsets=XY,
                       offset_transform=ax.transData)
```
