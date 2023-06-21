# Refine and Interpolate Data

We refine and interpolate the data using a `UniformTriRefiner`.

```python
# refining the data
refiner = UniformTriRefiner(tri)
tri_refi, z_test_refi = refiner.refine_field(z_test, subdiv=subdiv)
```

#
