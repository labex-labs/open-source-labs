# Создание графика с заштрихованными участками

Вы также можете использовать штриховку для участков в своем графике. В данном случае мы будем использовать функцию `fill_between`, чтобы создать заштрихованный участок.

```python
x = np.arange(0, 40, 0.2)
plt.fill_between(x, np.sin(x) * 4 + 30, y2=0, hatch='///', zorder=2, fc='c')
```
