# Создание весов выборок

Мы создадим два набора весов выборок. Первый набор весов выборок будет постоянным для всех точек, а второй набор весов выборок будет больше для некоторых выбросов.

```python
sample_weight_last_ten = abs(np.random.randn(len(X)))
sample_weight_constant = np.ones(len(X))
sample_weight_last_ten[15:] *= 5
sample_weight_last_ten[9] *= 15
```
