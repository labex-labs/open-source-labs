# Criar o Gráfico de Quiver

Com a grade e a direção das setas definidas, podemos criar o gráfico de quiver. Neste exemplo, usaremos a função `quiver` do Matplotlib para criar o gráfico. O parâmetro `length` define o comprimento das setas e o parâmetro `normalize` normaliza as setas para um comprimento de 1.

```python
ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
```
