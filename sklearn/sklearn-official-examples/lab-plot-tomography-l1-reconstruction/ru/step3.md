# Генерация данных

В этом шаге мы сгенерируем синтетические бинарные данные и проекции.

```python
l = 128
proj_operator = build_projection_operator(l, l // 7)
data = generate_synthetic_data()
proj = proj_operator @ data.ravel()[:, np.newaxis]
proj += 0.15 * np.random.randn(*proj.shape)
```
