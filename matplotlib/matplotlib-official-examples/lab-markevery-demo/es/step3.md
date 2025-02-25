# Crear gráficos con escalas logarítmicas

Repetimos el paso anterior, pero esta vez con escalas logarítmicas. Notamos que la escala logarítmica causa una asimetría visual en la distancia de los marcadores para la submuestreación basada en enteros, mientras que la submuestreación basada en fracciones crea distribuciones uniformes.

```python
# create plots with logarithmic scales
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```
