# Создание графика

Теперь мы готовы создать наш график. Мы будем использовать функцию `plot` из Matplotlib для построения трех линий на одном графике, каждая с предварительно определенной меткой. Мы будем использовать параметр `label` для присвоения меток каждой линии.

```python
# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(a, c, 'k--', label='Model length')
ax.plot(a, d, 'k:', label='Data length')
ax.plot(a, c + d, 'k', label='Total message length')
```
