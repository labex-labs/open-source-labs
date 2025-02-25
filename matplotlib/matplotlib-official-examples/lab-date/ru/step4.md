# Строим график данных

Мы построим график данных на всех трех подграфиках с использованием функции `plot`.

```python
for ax in axs:
    ax.plot('date', 'adj_close', data=data)
    ax.grid(True)
    ax.set_ylabel(r'Цена [\$]')
```
