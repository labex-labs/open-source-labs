# Создание подграфиков

Далее мы создадим два подграфика: один для выбросов и один для большинства данных. Мы будем использовать `plt.subplots` для создания подграфиков и установим параметр `sharex` в `True`, чтобы они имели общую ось x.

```python
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
```
