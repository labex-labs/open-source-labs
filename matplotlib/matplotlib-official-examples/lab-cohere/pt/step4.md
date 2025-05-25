# Plotar Coerência

Agora podemos plotar a coerência dos dois sinais usando a função `cohere` do Matplotlib.

```python
cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
axs[1].set_ylabel('Coherence')
```
