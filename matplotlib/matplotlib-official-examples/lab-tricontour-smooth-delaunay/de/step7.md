# Daten verfeinern und interpolieren

Wir verfeinern und interpolieren die Daten, indem wir einen `UniformTriRefiner` verwenden.

```python
# refining the data
refiner = UniformTriRefiner(tri)
tri_refi, z_test_refi = refiner.refine_field(z_test, subdiv=subdiv)
```
