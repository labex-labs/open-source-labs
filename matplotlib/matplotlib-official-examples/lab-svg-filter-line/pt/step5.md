# Definir Limites dos Eixos e Salvar a Figura

Definimos os limites x e y para os eixos e salvamos a figura como uma string de bytes no formato SVG usando `io.BytesIO()` e `plt.savefig()`.

```python
ax.set_xlim(0., 1.)
ax.set_ylim(0., 1.)

f = io.BytesIO()
plt.savefig(f, format="svg")
```
