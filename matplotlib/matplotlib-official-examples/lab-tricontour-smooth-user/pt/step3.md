# Refinar Dados (Refine Data)

Nesta etapa, usamos `tri.UniformTriRefiner` para refinar os dados. Usamos o método `refine_field` para refinar os valores `z` e criar uma nova Triangulação com maior resolução.

```python
refiner = tri.UniformTriRefiner(triang)
tri_refi, z_test_refi = refiner.refine_field(z, subdiv=3)
```
