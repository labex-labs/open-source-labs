# 데이터 정제 및 보간

`UniformTriRefiner`를 사용하여 데이터를 정제하고 보간합니다.

```python
# refining the data
refiner = UniformTriRefiner(tri)
tri_refi, z_test_refi = refiner.refine_field(z_test, subdiv=subdiv)
```
