# Subamostrar Imagem com Interpolação 'antialiased'

Em seguida, faremos a subamostragem da imagem de 450 pixels de dados para 125 ou 250 pixels usando a interpolação 'antialiased'. Isso demonstrará como o antialiasing pode ser usado para reduzir os padrões Moiré causados pela subamostragem de dados de alta frequência.

```python
fig, axs = plt.subplots(2, 2, figsize=(5, 6), layout='constrained')
axs[0, 0].imshow(a, interpolation='nearest', cmap='RdBu_r')
axs[0, 0].set_xlim(100, 200)
axs[0, 0].set_ylim(275, 175)
axs[0, 0].set_title('Zoom')

for ax, interp, space in zip(axs.flat[1:],
                             ['nearest', 'antialiased', 'antialiased'],
                             ['data', 'data', 'rgba']):
    ax.imshow(a, interpolation=interp, interpolation_stage=space,
              cmap='RdBu_r')
    ax.set_title(f"interpolation='{interp}'\nspace='{space}'")
plt.show()
```
