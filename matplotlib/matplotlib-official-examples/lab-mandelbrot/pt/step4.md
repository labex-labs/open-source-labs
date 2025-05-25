# Normalizar os Dados

Para criar uma renderização sombreada e com normalização de potência do conjunto de Mandelbrot, precisamos normalizar nossos dados. Faremos isso usando a seguinte fórmula:

`M = N + 1 - np.log2(np.log(abs(Z))) + log_horizon`

```python
with np.errstate(invalid='ignore'):
    M = np.nan_to_num(N + 1 - np.log2(np.log(abs(Z))) + log_horizon)
```
