# Refinar datos

```python
refiner = UniformTriRefiner(triang)
tri_refi, z_test_refi = refiner.refine_field(V, subdiv=3)
```

Explicación:

- `UniformTriRefiner` es una clase que refina una triangulación para crear una representación gráfica más precisa.
- `refiner` es una instancia de la clase `UniformTriRefiner`.
- `tri_refi` y `z_test_refi` son, respectivamente, la triangulación refinada y los valores del potencial.
