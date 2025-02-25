# Refinar datos

En este paso, utilizamos `tri.UniformTriRefiner` para refinar los datos. Utilizamos el método `refine_field` para refinar los valores de `z` y crear una nueva Triangulación con una resolución más alta.

```python
refiner = tri.UniformTriRefiner(triang)
tri_refi, z_test_refi = refiner.refine_field(z, subdiv=3)
```
