# Conectar dois pontos com uma seta

Nesta etapa, conectaremos os dois pontos com uma seta. Usaremos a função `annotate` para criar a seta e personalizaremos o estilo e a cor da seta.

```python
ax = axs.flat[0]
ax.plot([x1, x2], [y1, y2], ".")
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="-",
                            color="0.5",
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```
