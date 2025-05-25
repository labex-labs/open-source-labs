# Projetar Perfis de Contorno

Agora projetaremos os perfis de contorno nas paredes do gráfico. Isso é feito usando o método `contourf`. Definiremos o parâmetro `zdir` como 'z', 'x' e 'y' para projetar os perfis de contorno nas paredes z, x e y, respectivamente. Também definiremos o parâmetro `offset` para corresponder aos limites apropriados dos eixos.

```python
ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```
