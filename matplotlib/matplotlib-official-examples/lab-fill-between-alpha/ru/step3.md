# Выделение определенных областей с использованием `where`

Аргумент ключевого слова `where` очень удобен для выделения определенных областей графика. `where` принимает булевую маску той же длины, что и аргументы x, ymin и ymax, и заполняет только ту область, где булева маска имеет значение True. В следующем примере мы моделируем одного случайного блуждателя и вычисляем аналитическое среднее значение и стандартное отклонение позиций популяции. Среднее значение популяции показано пунктиром, а плюс/минус одно стандартное отклонение от среднего показано в виде заштрихованной области. Мы используем маску where `X > upper_bound`, чтобы найти область, где блуждатель находится за пределами одного стандартного отклонения, и закрашиваем эту область в красный цвет.

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
