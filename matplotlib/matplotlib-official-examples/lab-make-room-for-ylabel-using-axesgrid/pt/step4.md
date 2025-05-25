# Criar uma Figura com Dois Eixos

Nesta etapa, criamos uma figura com dois eixos. Usamos o método `add_axes` para adicionar dois eixos à figura. Também definimos o rótulo do y-tick para o primeiro eixo e o título para o segundo eixo.

```python
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 0.5])
ax2 = fig.add_axes([0, 0.5, 1, 0.5])

ax1.set_yticks([0.5], labels=["very long label"])
ax1.set_ylabel("Y label")

ax2.set_title("Title")
```
