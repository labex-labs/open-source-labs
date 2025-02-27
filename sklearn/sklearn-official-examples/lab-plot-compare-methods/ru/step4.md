# Multidimensional Scaling

Multidimensional scaling (MDS) ищет низкоразмерное представление данных, в котором расстояния хорошо соответствуют расстояниям в исходном высокомерном пространстве.

```python
md_scaling = manifold.MDS(
    n_components=n_components,
    max_iter=50,
    n_init=4,
    random_state=0,
    normalized_stress=False,
)
S_scaling = md_scaling.fit_transform(S_points)
```
