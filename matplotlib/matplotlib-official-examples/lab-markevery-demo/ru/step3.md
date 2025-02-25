# Создание графиков с логарифмическими шкалами

Мы повторяем предыдущий шаг, но на этот раз с логарифмическими шкалами. Мы замечаем, что логарифмическая шкала вызывает визуальную асимметрию в расстоянии между маркерами для выборки по целым числам, в то время как выборка по дробям создает равномерные распределения.

```python
# create plots with logarithmic scales
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```
