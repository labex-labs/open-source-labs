# Criar Gráficos com Escalas Logarítmicas

Repetimos o passo anterior, mas desta vez com escalas logarítmicas. Notamos que a escala logarítmica causa uma assimetria visual na distância do marcador para subamostragem baseada em inteiros, enquanto a subamostragem baseada em frações cria distribuições uniformes.

```python
# create plots with logarithmic scales
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```
