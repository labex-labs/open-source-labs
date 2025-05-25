# Utilizar o Algoritmo FastICA

Neste passo, utilizamos o algoritmo FastICA, que encontra direções no espaço de características correspondentes a projeções com alta não-gaussianidade.

```python
ica = FastICA(random_state=rng, whiten="arbitrary-variance")
S_ica_ = ica.fit(X).transform(X)  # Estimar as fontes

S_ica_ /= S_ica_.std(axis=0)
```
