# Создайте логарифмический график (лог-лог график) с настраиваемым диапазоном данных (datalim)

Далее мы создадим логарифмический график (лог-лог график) с настраиваемым диапазоном данных (datalim). Это означает, что и ось x, и ось y будут иметь логарифмические шкалы, и соотношение сторон графика будет настроено для соответствия данным.

```python
fig, ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_adjustable("datalim")
ax.plot([1, 3, 10], [1, 9, 100], "o-")
ax.set_xlim(1e-1, 1e2)
ax.set_ylim(1e-1, 1e3)
ax.set_aspect(1)
ax.set_title("Log-Log Plot with Adjustable Datalim")
plt.show()
```
