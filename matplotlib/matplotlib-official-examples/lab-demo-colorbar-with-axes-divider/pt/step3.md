# Adicionar uma barra de cores ao gráfico

Agora, adicionaremos uma barra de cores a cada subplot usando a função `make_axes_locatable` do Matplotlib. Esta função recebe um eixo existente, adiciona-o a um novo `AxesDivider` e retorna o `AxesDivider`. O método `append_axes` do `AxesDivider` pode então ser usado para criar um novo eixo em um determinado lado ("top", "right", "bottom" ou "left") do eixo original.

```python
ax1_divider = make_axes_locatable(ax1)
cax1 = ax1_divider.append_axes("right", size="7%", pad="2%")
cb1 = fig.colorbar(im1, cax=cax1)

ax2_divider = make_axes_locatable(ax2)
cax2 = ax2_divider.append_axes("top", size="7%", pad="2%")
cb2 = fig.colorbar(im2, cax=cax2, orientation="horizontal")
cax2.xaxis.set_ticks_position("top")
```
