# Уточните данные

```python
refiner = UniformTriRefiner(triang)
tri_refi, z_test_refi = refiner.refine_field(V, subdiv=3)
```

Пояснение:

- `UniformTriRefiner` - класс, который уточняет триангуляцию для создания более точной диаграммы.
- `refiner` - экземпляр класса `UniformTriRefiner`.
- `tri_refi` и `z_test_refi` - соответственно, уточненная триангуляция и значения потенциала.
