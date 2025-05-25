# Rótulos de marcação (tick labels) apontando para fora

Nesta etapa, criaremos um subplot com rótulos de marcação apontando para fora.

```python
fig = plt.figure(figsize=(6, 3))
fig.subplots_adjust(bottom=0.2)

ax = setup_axes(fig, 131)
for axis in ax.axis.values():
    axis.major_ticks.set_tick_out(True)
```
