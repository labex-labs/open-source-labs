# Utilisation de `alpha` pour atténuer les couleurs

L'argument `alpha` peut également être utilisé pour atténuer les couleurs pour des graphiques plus visuellement attrayants. Dans l'exemple suivant, nous allons calculer deux populations de marcheurs aléatoires avec une moyenne et une écart-type différentes des distributions normales à partir desquelles les pas sont tirés. Nous utilisons des régions remplies pour tracer +/- une écart-type de la position moyenne de la population.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

Nsteps, Nwalkers = 100, 250
t = np.arange(Nsteps)

# an (Nsteps x Nwalkers) array of random walk steps
S1 = 0.004 + 0.02*np.random.randn(Nsteps, Nwalkers)
S2 = 0.002 + 0.01*np.random.randn(Nsteps, Nwalkers)

# an (Nsteps x Nwalkers) array of random walker positions
X1 = S1.cumsum(axis=0)
X2 = S2.cumsum(axis=0)

# Nsteps length arrays empirical means and standard deviations of both
# populations over time
mu1 = X1.mean(axis=1)
sigma1 = X1.std(axis=1)
mu2 = X2.mean(axis=1)
sigma2 = X2.std(axis=1)

# plot it!
fig, ax = plt.subplots(1)
ax.plot(t, mu1, lw=2, label='moyenne population 1')
ax.plot(t, mu2, lw=2, label='moyenne population 2')
ax.fill_between(t, mu1+sigma1, mu1-sigma1, facecolor='C0', alpha=0.4)
ax.fill_between(t, mu2+sigma2, mu2-sigma2, facecolor='C1', alpha=0.4)
ax.set_title(r'marcheurs aléatoires $\mu$ empirique et intervalle $\pm \sigma$')
ax.legend(loc='upper left')
ax.set_xlabel('numéro de pas')
ax.set_ylabel('position')
ax.grid()
```
