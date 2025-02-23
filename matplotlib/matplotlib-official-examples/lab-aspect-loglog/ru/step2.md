# Создайте логарифмический график (лог-лог график) с настраиваемой рамкой

Далее мы создадим логарифмический график (лог-лог график) с настраиваемой рамкой. Это означает, что и ось x, и ось y будут иметь логарифмические шкалы, а соотношение сторон графика будет равно 1.

```python
fig, ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1e1, 1e3)
ax.set_ylim(1e2, 1e3)
ax.set_aspect(1)
ax.set_title("Log-Log Plot with Adjustable Box")
plt.show()
```
