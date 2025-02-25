# Créez l'axe des ordonnées secondaire

Nous allons créer un troisième exemple de relation entre les axes dans une transformation qui est ad hoc à partir des données et est dérivée empiriquement. Dans ce cas, nous allons définir les fonctions de transformation directe et inverse comme étant des interpolations linéaires d'un ensemble de données à l'autre.

```python
fig, ax = plt.subplots(layout='constrained')
xdata = np.arange(1, 11, 0.4)
ydata = np.random.randn(len(xdata))
ax.plot(xdata, ydata, label='Plotted data')

xold = np.arange(0, 11, 0.2)
# ensemble de données fictif reliant la coordonnée x à une autre coordonnée dérivée des données.
# xnew doit être monotone, donc nous le trions...
xnew = np.sort(10 * np.exp(-xold / 4) + np.random.randn(len(xold)) / 3)

ax.plot(xold[3:], xnew[3:], label='Transform data')
ax.set_xlabel('X [m]')
ax.legend()

def forward(x):
    return np.interp(x, xold, xnew)

def inverse(x):
    return np.interp(x, xnew, xold)

secax = ax.secondary_xaxis('top', functions=(forward, inverse))
secax.xaxis.set_minor_locator(AutoMinorLocator())
secax.set_xlabel('$X_{other}$')
```
