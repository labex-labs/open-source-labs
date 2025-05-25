# Adicionar Anotação de Forma

Agora adicionaremos uma anotação de forma ao gráfico. O código a seguir adicionará um retângulo em torno do segundo ponto de dados.

```python
bbox = dict(boxstyle="round", fc="0.8")
ax.annotate("Data Point 2", xy=(2, 4), xytext=(2.5, 4.5),
            bbox=bbox,
            arrowprops=dict(facecolor="black", shrink=0.05))
```
