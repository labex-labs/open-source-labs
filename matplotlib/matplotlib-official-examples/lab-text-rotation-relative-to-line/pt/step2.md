# Ajustar os limites do gráfico

Em seguida, ajustaremos os limites do gráfico para que a linha diagonal não esteja mais em um ângulo de 45 graus quando visualizada na tela. Isso criará um cenário em que precisamos rotacionar o texto em relação à linha, em vez do sistema de coordenadas da tela.

```python
# set limits so that it no longer looks on screen to be 45 degrees
ax.set_xlim([-10, 20])
```
