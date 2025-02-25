# 楕円の色を設定する

`EllipseCollection`内の各楕円の色を、そのx座標とy座標の合計に基づいて設定します。

```python
ec.set_array((X + Y).ravel())
```
