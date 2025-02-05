# Refine Data

In this step, we use `tri.UniformTriRefiner` to refine the data. We use the `refine_field` method to refine the `z` values and create a new Triangulation with higher resolution.

```python
refiner = tri.UniformTriRefiner(triang)
tri_refi, z_test_refi = refiner.refine_field(z, subdiv=3)
```
