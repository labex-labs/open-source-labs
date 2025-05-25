# Refinar os dados

```python
refiner = UniformTriRefiner(triang)
tri_refi, z_test_refi = refiner.refine_field(V, subdiv=3)
```

Explicação:

- `UniformTriRefiner` é uma classe que refina uma triangulação para criar um gráfico mais preciso.
- `refiner` é uma instância da classe `UniformTriRefiner`.
- `tri_refi` e `z_test_refi` são, respectivamente, a triangulação refinada e os valores de potencial.
