# Gerar Dados

Geramos alguns dados de amostra para serem plotados. Aqui, usamos a biblioteca `numpy` para gerar três arrays de dados.

```python
t = np.arange(0.0, 2.0, 0.01)

s1 = np.sin(2 * np.pi * t)
s2 = np.exp(-t)
s3 = s1 * s2
```
