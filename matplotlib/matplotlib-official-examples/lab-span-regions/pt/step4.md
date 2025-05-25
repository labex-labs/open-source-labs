# Sombrear as Regiões

Usaremos `fill_between` para sombrear as regiões acima e abaixo da linha horizontal onde a onda senoidal é positiva e negativa, respectivamente.

```python
ax.fill_between(t, 1, where=s > 0, facecolor='green', alpha=.5)
ax.fill_between(t, -1, where=s < 0, facecolor='red', alpha=.5)
```
