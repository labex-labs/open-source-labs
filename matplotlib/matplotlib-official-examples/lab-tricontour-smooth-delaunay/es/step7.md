# Mezclar y interpolar datos

Mezclamos e interpolamos los datos utilizando un `UniformTriRefiner`.

```python
# Mezclando los datos
refiner = UniformTriRefiner(tri)
tri_refi, z_test_refi = refiner.refine_field(z_test, subdiv=subdiv)
```
