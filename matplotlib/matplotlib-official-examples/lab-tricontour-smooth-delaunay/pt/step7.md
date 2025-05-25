# Refinar e Interpolar Dados

Nós refinamos e interpolamos os dados usando um `UniformTriRefiner`.

```python
# refining the data
refiner = UniformTriRefiner(tri)
tri_refi, z_test_refi = refiner.refine_field(z_test, subdiv=subdiv)
```
