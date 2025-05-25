# Criar Gráfico de Contorno

Agora criaremos o gráfico de contorno usando a função `contour()`. Passaremos os dados `X`, `Y` e `Z` e definiremos `extend3d=True` para estender as curvas verticalmente em "fitas" (ribbons). Também definiremos o mapa de cores para `cm.coolwarm` para um esquema de cores agradável.

```python
ax.contour(X, Y, Z, extend3d=True, cmap=cm.coolwarm)
```
