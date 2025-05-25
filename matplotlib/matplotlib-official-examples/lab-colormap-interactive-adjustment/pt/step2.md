# Gerar Dados

Em seguida, você gerará alguns dados de exemplo. Neste laboratório, geraremos uma onda senoidal bidimensional.

```python
t = np.linspace(0, 2 * np.pi, 1024)
data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :]
```
