# Affiner les données

```python
refiner = UniformTriRefiner(triang)
tri_refi, z_test_refi = refiner.refine_field(V, subdiv=3)
```

Explication :

- `UniformTriRefiner` est une classe qui affine une triangulation pour créer un tracé plus précis.
- `refiner` est une instance de la classe `UniformTriRefiner`.
- `tri_refi` et `z_test_refi` sont respectivement la triangulation affinée et les valeurs de potentiel.
