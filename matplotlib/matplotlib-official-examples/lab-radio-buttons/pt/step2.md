# Criar Dados

Em seguida, criaremos os dados que serão usados no gráfico. Criaremos três diferentes ondas senoidais com diferentes frequências usando a biblioteca `numpy`.

```python
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(8*np.pi*t)
```
