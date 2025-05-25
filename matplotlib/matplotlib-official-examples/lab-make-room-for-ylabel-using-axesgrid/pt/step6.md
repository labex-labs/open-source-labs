# Criar uma Figura com Dois Eixos Ajustáveis

Nesta etapa, criamos uma figura com dois eixos ajustáveis. Usamos o método `make_axes_locatable` para criar um divisor que permite que os eixos sejam ajustados. Adicionamos um novo eixo à direita do primeiro eixo usando o método `append_axes`.

```python
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 1])
divider = make_axes_locatable(ax1)
ax2 = divider.append_axes("right", "100%", pad=0.3, sharey=ax1)
fig.add_axes(ax2)
```
