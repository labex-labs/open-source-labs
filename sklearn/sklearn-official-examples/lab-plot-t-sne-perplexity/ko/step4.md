# t-SNE 적용

다음으로, 동심원 데이터셋에 t-SNE 를 적용합니다.

```python
t0 = time()
tsne = manifold.TSNE(
    n_components=n_components,
    init="random",
    random_state=0,
    perplexity=perplexity,
    n_iter=300,
)
Y = tsne.fit_transform(X)
t1 = time()
```
