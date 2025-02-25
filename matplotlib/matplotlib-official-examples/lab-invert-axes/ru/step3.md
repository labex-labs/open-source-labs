# Построить график

Теперь мы можем построить график с использованием Matplotlib. Мы будем использовать функцию `plot` для построения наших данных и задавать пределы оси x с использованием функции `set_xlim`.

```python
fig, ax = plt.subplots()

ax.plot(t, s)
ax.set_xlim(5, 0)  # decreasing time
ax.set_xlabel('decreasing time (s)')
ax.set_ylabel('voltage (mV)')
ax.set_title('Should be growing...')
ax.grid(True)

plt.show()
```
