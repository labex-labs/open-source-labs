# Criar Dados para os Gráficos

Precisamos criar dados para os gráficos a serem visualizados. Neste exemplo, criaremos três conjuntos de dados diferentes usando NumPy.

```python
t = np.arange(0.01, 5.0, 0.01)
s1 = np.sin(2 * np.pi * t)
s2 = np.exp(-t)
s3 = np.sin(4 * np.pi * t)
```
