# 球体の作成

次に、プロットの中心から一定距離以内にある RGB 値の条件を定義することで、プロット内に球体を作成します。

```python
rc = midpoints(r)
gc = midpoints(g)
bc = midpoints(b)

sphere = (rc - 0.5)**2 + (gc - 0.5)**2 + (bc - 0.5)**2 < 0.5**2
```
