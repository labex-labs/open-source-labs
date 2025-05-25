# Alinhar os Rótulos do Eixo Y Manualmente

O quarto passo é alinhar os rótulos do eixo y manualmente usando o método `~.Axis.set_label_coords` do objeto do eixo y.

```python
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, wspace=0.6)
make_plot(axs)

labex = -0.3  # axes coords

for j in range(2):
    axs[j, 1].yaxis.set_label_coords(labex, 0.5)

plt.show()
```
