# Plotar Dados

Agora que criamos nossos subplots, podemos plotar nossos dados usando `np.sin(x)`.

```python
x = np.arange(0, 2*np.pi, 0.01)
ax0.plot(x, np.sin(x))
ax1.plot(x, np.sin(x))
```
