# Adicionar Botões de Seleção (Check Buttons)

Agora, adicionaremos os botões de seleção ao nosso gráfico usando a função `CheckButtons`. Passaremos as linhas plotadas como rótulos e definiremos a visibilidade inicial de cada linha. Também ajustaremos as propriedades dos botões de seleção para corresponder às cores das linhas plotadas.

```python
lines_by_label = {l.get_label(): l for l in [l0, l1, l2]}
line_colors = [l.get_color() for l in lines_by_label.values()]

rax = fig.add_axes([0.05, 0.4, 0.1, 0.15])
check = CheckButtons(
    ax=rax,
    labels=lines_by_label.keys(),
    actives=[l.get_visible() for l in lines_by_label.values()],
    label_props={'color': line_colors},
    frame_props={'edgecolor': line_colors},
    check_props={'facecolor': line_colors},
)
```
