# Диаграмма рассеяния с режимом автоматической настройки делений round_numbers

В этом шаге мы переключим `axes.autolimit_mode` в 'round_numbers' и создадим диаграмму рассеяния, чтобы деления были в округленных числах и были также на краях.

```python
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'

fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
plt.show()
```
