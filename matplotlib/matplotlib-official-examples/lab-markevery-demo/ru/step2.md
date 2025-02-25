# Создание графиков с линейными шкалами

Далее мы создаем набор подграфиков, чтобы показать, как ведет себя `markevery` с линейными шкалами. Мы перебираем список `cases` и строим каждый случай на отдельном подграфике. Мы используем параметр `markevery`, чтобы указать, какие точки данных следует помечать.

```python
# create plots with linear scales
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```
