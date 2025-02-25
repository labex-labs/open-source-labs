# データの微調整と補間

`UniformTriRefiner`を使用して、データを微調整し補間します。

```python
# refining the data
refiner = UniformTriRefiner(tri)
tri_refi, z_test_refi = refiner.refine_field(z_test, subdiv=subdiv)
```
