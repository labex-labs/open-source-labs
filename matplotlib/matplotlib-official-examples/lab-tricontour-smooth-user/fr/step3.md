# Raffinement des données

Dans cette étape, nous utilisons `tri.UniformTriRefiner` pour raffiner les données. Nous utilisons la méthode `refine_field` pour raffiner les valeurs de `z` et créer une nouvelle triangulation avec une résolution plus élevée.

```python
refiner = tri.UniformTriRefiner(triang)
tri_refi, z_test_refi = refiner.refine_field(z, subdiv=3)
```
