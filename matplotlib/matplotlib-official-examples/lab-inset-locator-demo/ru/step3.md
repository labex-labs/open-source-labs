# Отключить метки делений

Чтобы удалить метки делений из каждой вставки, мы можем использовать метод `tick_params()` и установить `labelleft` и `labelbottom` в `False`.

```python
# Отключить метки делений вставок
for axi in [axins, axins2, axins3, axins4]:
    axi.tick_params(labelleft=False, labelbottom=False)
```
