# Escalonamento Multidimensional

O escalonamento multidimensional (MDS) busca uma representação de baixa dimensão dos dados na qual as distâncias respeitem bem as distâncias no espaço original de alta dimensão.

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
