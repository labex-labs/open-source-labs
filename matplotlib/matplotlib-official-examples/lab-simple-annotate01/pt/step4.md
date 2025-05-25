# Adicionar Anotação de Seta

Agora adicionaremos uma anotação de seta ao gráfico. O código a seguir adicionará uma seta do primeiro ponto de dados para o segundo ponto de dados.

```python
ax.annotate("", xy=(1, 3), xytext=(2, 4),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
```
