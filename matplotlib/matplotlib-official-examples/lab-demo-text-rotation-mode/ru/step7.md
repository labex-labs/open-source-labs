# Создаем подфигуры и вызываем функцию `test_rotation_mode`

Мы создадим две подфигуры и вызовем функцию `test_rotation_mode` с параметрами `fig` и `mode`.

```python
fig = plt.figure(figsize=(8, 5))
subfigs = fig.subfigures(1, 2)
test_rotation_mode(subfigs[0], "default")
test_rotation_mode(subfigs[1], "anchor")
plt.show()
```
