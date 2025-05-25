# Criar Eixos Flutuantes (Floating Axes)

Nesta etapa, criaremos dois eixos flutuantes que serão usados para exibir a curva polar em uma caixa retangular. Usaremos `new_floating_axis()` para criar os eixos flutuantes.

```python
# Create the floating axes
ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 60)
axis.label.set_text(r"$\theta = 60^{\circ}$")
axis.label.set_visible(True)

ax1.axis["lon"] = axis = ax1.new_floating_axis(1, 6)
axis.label.set_text(r"$r = 6$")
```
