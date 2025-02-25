# Создаем график и подключаем слушателя событий нажатия клавиши

Создадим простой график с использованием `np.random.rand()` для генерации случайных данных. Затем настроим слушателя событий нажатия клавиши с использованием `fig.canvas.mpl_connect()`, передав имя события, на которое мы хотим слушать (`'key_press_event'`), и функцию, которую мы хотим вызвать при наступлении события (`on_press`).

```python
fig, ax = plt.subplots()

fig.canvas.mpl_connect('key_press_event', on_press)

ax.plot(np.random.rand(12), np.random.rand(12), 'go')
xl = ax.set_xlabel('easy come, easy go')
ax.set_title('Press a key')
plt.show()
```
