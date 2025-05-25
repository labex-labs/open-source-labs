# Adicionando Anotações ao Gráfico

Podemos adicionar anotações ao gráfico usando a função `ax.annotate()`. Esta função recebe três argumentos: o texto da anotação, a coordenada xy do ponto a ser anotado e a coordenada xy da posição do texto. Podemos personalizar o estilo da anotação usando o argumento `arrowprops`.

```python
ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))
```
