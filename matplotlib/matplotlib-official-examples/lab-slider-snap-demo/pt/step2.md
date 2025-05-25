# Gerar Dados

Nesta etapa, você gerará os dados a serem plotados. Você criará uma onda senoidal com uma frequência de 3 Hz e uma amplitude de 5.

```python
t = np.arange(0.0, 1.0, 0.001)
a0 = 5
f0 = 3
s = a0 * np.sin(2 * np.pi * f0 * t)
```
