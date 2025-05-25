# Gerar Dados

Em seguida, geraremos os dados para o nosso gráfico. Criaremos três ondas senoidais com diferentes frequências usando `numpy`.

```python
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(6*np.pi*t)
```
