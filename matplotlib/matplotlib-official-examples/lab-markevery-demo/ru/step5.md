# Создание полярных графиков

Наконец, мы создаем набор подграфиков, чтобы показать, как ведет себя `markevery` на полярных графиках. Мы замечаем, что поведение аналогично поведению на линейных шкалах.

```python
# create polar plots
r = np.linspace(0, 3.0, 200)
theta = 2 * np.pi * r

fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained',
                        subplot_kw={'projection': 'polar'})
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(theta, r, 'o', ls='-', ms=4, markevery=markevery)
```
