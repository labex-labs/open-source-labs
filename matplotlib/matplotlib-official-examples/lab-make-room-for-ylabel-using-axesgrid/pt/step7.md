# Ajustar os Eixos e Criar Espaço para o Rótulo do Eixo Y

Nesta etapa, usamos o método `add_auto_adjustable_area` para ajustar os eixos e criar espaço para o rótulo do eixo y. Também definimos o título e o rótulo do eixo x para o segundo eixo.

```python
divider.add_auto_adjustable_area(use_axes=[ax1], pad=0.1,
                                 adjust_dirs=["left"])
divider.add_auto_adjustable_area(use_axes=[ax2], pad=0.1,
                                 adjust_dirs=["right"])
divider.add_auto_adjustable_area(use_axes=[ax1, ax2], pad=0.1,
                                 adjust_dirs=["top", "bottom"])

ax1.set_yticks([0.5], labels=["very long label"])
ax2.set_title("Title")
ax2.set_xlabel("X - Label")
```
