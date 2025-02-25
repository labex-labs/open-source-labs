# Mise en évidence de certaines régions avec `where`

L'argument clé `where` est très pratique pour mettre en évidence certaines régions du graphique. `where` prend un masque booléen de la même longueur que les arguments x, ymin et ymax, et ne remplit que la région où le masque booléen est True. Dans l'exemple ci-dessous, nous simulons un seul marcheur aléatoire et calculons la moyenne analytique et l'écart-type des positions de la population. La moyenne de la population est représentée par la ligne pointillée, et l'écart de plus ou moins un écart-type par rapport à la moyenne est représenté par la région remplie. Nous utilisons le masque where `X > upper_bound` pour trouver la région où le marcheur est en dehors de la limite d'un écart-type, et nous colorons cette région en rouge.

```python
# Fixing random state for reproducibility
np.random.seed(1)

Nsteps = 500
t = np.arange(Nsteps)

mu = 0.002
sigma = 0.01

# les pas et la position
S = mu + sigma*np.random.randn(Nsteps)
X = S.cumsum()

# les bornes analytiques inférieure et supérieure de la population d'un écart-type
lower_bound = mu*t - sigma*np.sqrt(t)
upper_bound = mu*t + sigma*np.sqrt(t)

fig, ax = plt.subplots(1)
ax.plot(t, X, lw=2, label='position du marcheur')
ax.plot(t, mu*t, lw=1, label='moyenne de la population', color='C0', ls='--')
ax.fill_between(t, lower_bound, upper_bound, facecolor='C0', alpha=0.4,
                label='plage d\'un écart-type')
ax.legend(loc='upper left')

# ici, nous utilisons l'argument where pour ne remplir que la région où le
# marcheur est au-dessus de la limite d'un écart-type de la population
ax.fill_between(t, upper_bound, X, where=X > upper_bound, fc='red', alpha=0.4)
ax.fill_between(t, lower_bound, X, where=X < lower_bound, fc='red', alpha=0.4)
ax.set_xlabel('numéro de pas')
ax.set_ylabel('position')
ax.grid()
```
