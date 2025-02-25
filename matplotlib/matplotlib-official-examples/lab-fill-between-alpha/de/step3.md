# Das Hervorheben bestimmter Bereiche mit `where`

Das Schlüsselwortargument `where` ist sehr praktisch, um bestimmte Bereiche des Graphen hervorzuheben. `where` nimmt eine boolesche Maske der gleichen Länge wie die x-, ymin- und ymax-Argumente entgegen und füllt nur den Bereich aus, in dem die boolesche Maske True ist. Im folgenden Beispiel simulieren wir einen einzelnen Zufallswalker und berechnen den analytischen Mittelwert und die Standardabweichung der Populationspositionen. Der Populationsmittelwert wird als gestrichelte Linie gezeigt, und die Plus/Minus-Eine-Standardabweichung vom Mittelwert wird als gefüllter Bereich gezeigt. Wir verwenden die where-Maske `X > upper_bound`, um den Bereich zu finden, in dem der Walker außerhalb der einen-Standardabweichungsgrenze ist, und färben diesen Bereich rot ein.

```python
# Fixing random state for reproducibility
np.random.seed(1)

Nsteps = 500
t = np.arange(Nsteps)

mu = 0.002
sigma = 0.01

# the steps and position
S = mu + sigma*np.random.randn(Nsteps)
X = S.cumsum()

# the 1 sigma upper and lower analytic population bounds
lower_bound = mu*t - sigma*np.sqrt(t)
upper_bound = mu*t + sigma*np.sqrt(t)

fig, ax = plt.subplots(1)
ax.plot(t, X, lw=2, label='walker position')
ax.plot(t, mu*t, lw=1, label='population mean', color='C0', ls='--')
ax.fill_between(t, lower_bound, upper_bound, facecolor='C0', alpha=0.4,
                label='1 sigma range')
ax.legend(loc='upper left')

# here we use the where argument to only fill the region where the
# walker is above the population 1 sigma boundary
ax.fill_between(t, upper_bound, X, where=X > upper_bound, fc='red', alpha=0.4)
ax.fill_between(t, lower_bound, X, where=X < lower_bound, fc='red', alpha=0.4)
ax.set_xlabel('num steps')
ax.set_ylabel('position')
ax.grid()
```
