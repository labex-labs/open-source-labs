# Adicionar Anotação de Texto

Agora adicionaremos uma anotação de texto ao gráfico. O código a seguir adicionará o texto "Data Point 1" no primeiro ponto de dados.

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05))
```
