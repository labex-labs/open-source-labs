# Создаем объекты Figure и Axes

Теперь мы создадим объекты Figure и Axes с использованием метода `add_subplot()`. Мы установим параметр `projection` в `'3d'`, чтобы создать трехмерный график.

```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
```
