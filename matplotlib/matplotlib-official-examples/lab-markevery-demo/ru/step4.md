# Создание масштабированных графиков

Мы создаем еще один набор подграфиков, на этот раз, чтобы показать, как ведет себя `markevery` на масштабированных графиках. Мы замечаем, что выборка по целым числам выбирает точки из исходных данных и не зависит от вида, в то время как выборка по вещественным числам связана с диагональю осей и изменяет диапазон отображаемых данных.

```python
# create zoomed plots
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
    ax.set_xlim((6, 6.7))
    ax.set_ylim((1.1, 1.7))
```
