# Создание графика

Далее мы создадим график с использованием функции `subplots()` из Matplotlib и построим график изменения цены закрытия акций Google с учетом корректировок в течение времени.

```python
fig, ax = plt.subplots()
ax.plot(r.date, r.adj_close)
```
