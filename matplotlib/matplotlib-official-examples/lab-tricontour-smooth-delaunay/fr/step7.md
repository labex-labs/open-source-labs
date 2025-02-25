# Affiner et interpoler les données

Nous affinons et interpolons les données à l'aide d'un `UniformTriRefiner`.

```python
# raffinement des données
refiner = UniformTriRefiner(tri)
tri_refi, z_test_refi = refiner.refine_field(z_test, subdiv=subdiv)
```
