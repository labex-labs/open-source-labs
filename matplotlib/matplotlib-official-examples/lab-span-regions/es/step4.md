# Sombra las regiones

Utilizaremos `fill_between` para sombrear las regiones por encima y por debajo de la línea horizontal donde la onda senoidal es positiva y negativa, respectivamente.

```python
ax.fill_between(t, 1, where=s > 0, facecolor='green', alpha=.5)
ax.fill_between(t, -1, where=s < 0, facecolor='red', alpha=.5)
```
