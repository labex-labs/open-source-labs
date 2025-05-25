# Mudando a Direção do Eixo

Agora, criaremos um loop para configurar quatro gráficos diferentes com o eixo flutuante em cada uma das quatro direções cardinais. No loop, usaremos `add_floating_axis1()` e `add_floating_axis2()` para adicionar os eixos flutuantes, e `set_axis_direction()` para definir a direção do eixo.

```python
fig = plt.figure(figsize=(8, 4), layout="constrained")

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=241+i)
    axis = add_floating_axis1(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=245+i)
    axis = add_floating_axis2(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

plt.show()
```
