# Refine data

```python
refiner = UniformTriRefiner(triang)
tri_refi, z_test_refi = refiner.refine_field(V, subdiv=3)
```

Explanation:

- `UniformTriRefiner` is a class that refines a triangulation to create a more accurate plot.
- `refiner` is an instance of the `UniformTriRefiner` class.
- `tri_refi` and `z_test_refi` are refined triangulation and potential values, respectively.
