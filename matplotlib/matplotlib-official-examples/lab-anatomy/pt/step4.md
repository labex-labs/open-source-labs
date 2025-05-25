# Adicionar rótulos e título

Agora adicionaremos rótulos aos eixos x e y, e um título à figura usando os métodos `set_xlabel()`, `set_ylabel()` e `set_title()`.

```python
# Add labels and title
ax.set_xlabel("x Axis label", fontsize=14)
ax.set_ylabel("y Axis label", fontsize=14)
ax.set_title("Anatomy of a figure", fontsize=20, verticalalignment='bottom')
```
