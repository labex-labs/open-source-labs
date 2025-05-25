# Criar o Gráfico de Contorno

Agora criaremos o gráfico de contorno usando o método `contourf()`. Este método cria contornos preenchidos. Definiremos o parâmetro `cmap` como `cm.coolwarm` para usar o mapa de cores cool-warm.

```python
ax.contourf(X, Y, Z, cmap=cm.coolwarm)
```
