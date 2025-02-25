# Создаем внутренний gridspec

Теперь мы создадим внутренний gridspec. Мы будем использовать метод `GridSpecFromSubplotSpec`, чтобы создать gridspec размером 3 на 3, который будет подграфиком внешнего gridspec.

```python
gs00 = gridspec.GridSpecFromSubplotSpec(3, 3, subplot_spec=gs0[0])
```
