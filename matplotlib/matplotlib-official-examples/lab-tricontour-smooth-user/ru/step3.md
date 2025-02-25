# Уточнение данных

В этом шаге мы используем `tri.UniformTriRefiner` для уточнения данных. Мы используем метод `refine_field` для уточнения значений `z` и создания новой триангуляции с более высоким разрешением.

```python
refiner = tri.UniformTriRefiner(triang)
tri_refi, z_test_refi = refiner.refine_field(z, subdiv=3)
```
