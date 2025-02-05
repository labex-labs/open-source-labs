# 细化和插值数据

我们使用 `UniformTriRefiner` 来细化和插值数据。

```python
# refining the data
refiner = UniformTriRefiner(tri)
tri_refi, z_test_refi = refiner.refine_field(z_test, subdiv=subdiv)
```
