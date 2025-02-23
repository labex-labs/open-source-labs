#Comparer les graphiques "asinh" avec différents paramètres d'échelle "linear_width"

Nous allons maintenant comparer les graphiques "asinh" avec différents paramètres d'échelle "linear_width". Nous allons tracer trois graphiques avec différentes valeurs de "linear_width".

```python
fig2 = plt.figure(layout='constrained')
axs = fig2.subplots(1, 3, sharex=True)
for ax, (a0, base) in zip(axs, ((0.2, 2), (1.0, 0), (5.0, 10))):
    ax.set_title(f'largeur linéaire={a0:.3g}')
    ax.plot(x, x, label='y=x')
    ax.plot(x, 10*x, label='y=10x')
    ax.plot(x, 100*x, label='y=100x')
    ax.set_yscale('asinh', largeur_linéaire=a0, base=base)
    ax.grid()
    ax.legend(loc='best', taille police='petite')
```
