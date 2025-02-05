# 细化数据

在这一步中，我们使用`tri.UniformTriRefiner`来细化数据。我们使用`refine_field`方法来细化`z`值，并创建一个具有更高分辨率的新三角剖分。

```python
refiner = tri.UniformTriRefiner(triang)
tri_refi, z_test_refi = refiner.refine_field(z, subdiv=3)
```
