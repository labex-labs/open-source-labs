# デロネ三角分割を行う

`matplotlib.tri`モジュールの`Triangulation`関数を使って、テスト用のデータポイントに対してデロネ三角分割を行います。

```python
# meshing with Delaunay triangulation
tri = Triangulation(x_test, y_test)
ntri = tri.triangles.shape[0]
```
