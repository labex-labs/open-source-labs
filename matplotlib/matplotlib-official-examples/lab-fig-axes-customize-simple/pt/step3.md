# Adicionando eixos à figura

Adicionaremos eixos à figura usando o método `fig.add_axes()`. Também definiremos a cor de fundo dos eixos usando o método `rect.set_facecolor()`.

```python
ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.4])
rect = ax1.patch
rect.set_facecolor('lightslategray')
```
