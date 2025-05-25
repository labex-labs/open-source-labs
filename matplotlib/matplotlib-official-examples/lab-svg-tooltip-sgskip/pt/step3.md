# Salvar a figura como SVG

Salvamos a figura em um objeto de arquivo falso usando a classe `BytesIO` e o método `savefig`.

```python
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_aspect('equal')

f = BytesIO()
plt.savefig(f, format="svg")
```
