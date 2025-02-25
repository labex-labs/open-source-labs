# Tracer la cohérence

Nous pouvons maintenant tracer la cohérence des deux signaux à l'aide de la fonction `cohere` de Matplotlib.

```python
cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
axs[1].set_ylabel('Cohérence')
```
