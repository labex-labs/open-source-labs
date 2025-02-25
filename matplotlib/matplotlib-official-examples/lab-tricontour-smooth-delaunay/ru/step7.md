# Уточнить и интерполировать данные

Мы уточняем и интерполируем данные с использованием `UniformTriRefiner`.

```python
# refining the data
refiner = UniformTriRefiner(tri)
tri_refi, z_test_refi = refiner.refine_field(z_test, subdiv=subdiv)
```
