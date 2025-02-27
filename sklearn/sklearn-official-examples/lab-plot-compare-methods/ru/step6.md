# T-distributed Stochastic Neighbor Embedding

Оно преобразует сходства между точками данных в совместные вероятности и пытается минимизировать дивергенцию Куллбека-Лейблера между совместными вероятностями низкоразмерного встраивания и высокомерных данных.

```python
t_sne = manifold.TSNE(
    n_components=n_components,
    perplexity=30,
    init="random",
    n_iter=250,
    random_state=0,
)
S_t_sne = t_sne.fit_transform(S_points)
```
