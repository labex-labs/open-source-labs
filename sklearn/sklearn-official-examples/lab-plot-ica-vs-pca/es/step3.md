# Utilizar el algoritmo FastICA

En este paso, utilizamos el algoritmo FastICA, que encuentra direcciones en el espacio de características correspondientes a proyecciones con alta no gaussianidad.

```python
ica = FastICA(random_state=rng, whiten="arbitrary-variance")
S_ica_ = ica.fit(X).transform(X)  # Estimar las fuentes

S_ica_ /= S_ica_.std(axis=0)
```
