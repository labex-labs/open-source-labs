# Graficar coherencia

Ahora podemos graficar la coherencia de las dos señales utilizando la función `cohere` de Matplotlib.

```python
cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
axs[1].set_ylabel('Coherence')
```
