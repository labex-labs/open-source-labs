# Ajustar o Preenchimento do Rótulo do Eixo

Nesta etapa, ajuste o preenchimento do rótulo do eixo no eixo flutuante. Isso pode ser feito definindo o atributo `pad` do objeto `label` para o valor de preenchimento desejado.

```python
# Adjust Axis Label Padding
fig = plt.figure(figsize=(9, 3.))
fig.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99, wspace=0.01, hspace=0.01)

ax1 = setup_axes(fig, rect=121)
axis = add_floating_axis(ax1)

ax1 = setup_axes(fig, rect=122)
axis = add_floating_axis(ax1)
axis.label.set_pad(20)

plt.show()
```
