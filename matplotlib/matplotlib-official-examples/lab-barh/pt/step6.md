# Personalizar o Gráfico

Para tornar o gráfico mais informativo, podemos personalizá-lo adicionando rótulos, título e invertendo o eixo y.

```python
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')
```
