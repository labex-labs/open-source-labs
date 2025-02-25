# Удаление отдельных компонентов

Мы можем удалить отдельные компоненты диаграммы "ящик с усами", используя различные ключевые аргументы, доступные в функции `boxplot()`. Например, мы можем удалить средние значения, установив `showmeans` в False. Также мы можем удалить коробку и усики, установив `showbox` и `showcaps` в False соответственно.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 8), sharey=True)
axs[0, 0].boxplot(data, labels=labels)
axs[0, 0].set_title('Default')

axs[0, 1].boxplot(data, labels=labels, showmeans=False)
axs[0, 1].set_title('No Means')

axs[1, 0].boxplot(data, labels=labels, showbox=False, showcaps=False)
axs[1, 0].set_title('No Box or Whiskers')

axs[1, 1].boxplot(data, labels=labels, showfliers=False)
axs[1, 1].set_title('No Outliers')

plt.show()
```
