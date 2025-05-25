# Destacando Certas Regiões com `where`

O argumento de palavra-chave `where` é muito útil para destacar certas regiões do gráfico. `where` recebe uma máscara booleana com o mesmo comprimento dos argumentos x, ymin e ymax, e preenche apenas a região onde a máscara booleana é True. No exemplo abaixo, simulamos um único caminhante aleatório e calculamos a média analítica e o desvio padrão das posições da população. A média da população é mostrada como a linha tracejada, e o desvio de mais/menos um sigma da média é mostrado como a região preenchida. Usamos a máscara where `X > upper_bound` para encontrar a região onde o caminhante está fora do limite de um sigma, e sombreamos essa região em vermelho.

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
