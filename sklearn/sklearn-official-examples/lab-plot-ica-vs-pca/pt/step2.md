# Utilizar o Algoritmo PCA

Neste passo, utilizamos o algoritmo PCA para encontrar direções ortogonais no espaço de características bruto que correspondem a direções que explicam a máxima variância.

```python
pca = PCA()
S_pca_ = pca.fit(X).transform(X)
```
