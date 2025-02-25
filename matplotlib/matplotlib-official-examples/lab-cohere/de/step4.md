# Kohärenz darstellen

Wir können nun die Kohärenz der beiden Signale mit der `cohere`-Funktion von Matplotlib darstellen.

```python
cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
axs[1].set_ylabel('Kohärenz')
```
