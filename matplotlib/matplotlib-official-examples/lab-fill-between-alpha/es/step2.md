# Uso de `alpha` para suavizar los colores

El argumento `alpha` también se puede utilizar para suavizar los colores en gráficos más atractivos visualmente. En el siguiente ejemplo, calcularemos dos poblaciones de caminantes aleatorios con una media y desviación estándar diferentes de las distribuciones normales de las que se extraen los pasos. Utilizamos regiones rellenas para trazar +/- una desviación estándar de la posición media de la población.

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
ax.plot(t, mu1, lw=2, label='media de la población 1')
ax.plot(t, mu2, lw=2, label='media de la población 2')
ax.fill_between(t, mu1+sigma1, mu1-sigma1, facecolor='C0', alpha=0.4)
ax.fill_between(t, mu2+sigma2, mu2-sigma2, facecolor='C1', alpha=0.4)
ax.set_title(r'caminantes aleatorios, media empírica $\mu$ y intervalo $\pm \sigma$')
ax.legend(loc='upper left')
ax.set_xlabel('número de pasos')
ax.set_ylabel('posición')
ax.grid()
```
