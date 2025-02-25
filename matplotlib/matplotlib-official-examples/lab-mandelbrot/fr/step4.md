# Normaliser les données

Pour créer une représentation ombrée et normalisée en puissance de l'ensemble de Mandelbrot, nous devons normaliser nos données. Nous le ferons en utilisant la formule suivante :

`M = N + 1 - np.log2(np.log(abs(Z))) + log_horizon`

```python
with np.errstate(invalid='ignore'):
    M = np.nan_to_num(N + 1 - np.log2(np.log(abs(Z))) + log_horizon)
```
