# Personalizar Anotações

Podemos personalizar as anotações alterando o tamanho da fonte, a cor da fonte e o estilo da seta. O código a seguir alterará o tamanho da fonte, a cor da fonte e o estilo da seta da anotação de texto.

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05, arrowstyle="->"),
            fontsize=12, color="red")
```
