# Desenhar setas no final dos _spines_

Para indicar a direção dos eixos, você pode desenhar setas no final dos _spines_.

```python
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
```
