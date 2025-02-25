# データの微調整

このステップでは、`tri.UniformTriRefiner`を使ってデータを微調整します。`refine_field`メソッドを使って`z`値を微調整し、より高解像度の新しいTriangulationを作成します。

```python
refiner = tri.UniformTriRefiner(triang)
tri_refi, z_test_refi = refiner.refine_field(z, subdiv=3)
```
