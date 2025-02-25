# Normalizar los datos

Para crear una representación iluminada y normalizada en potencia del conjunto de Mandelbrot, necesitamos normalizar nuestros datos. Lo haremos utilizando la siguiente fórmula:

`M = N + 1 - np.log2(np.log(abs(Z))) + log_horizon`

```python
with np.errstate(invalid='ignore'):
    M = np.nan_to_num(N + 1 - np.log2(np.log(abs(Z))) + log_horizon)
```
