# Установить эпоху по новому умолчанию

Для использования современных дат с точностью до микросекунд нам нужно установить эпоху по новому умолчанию, то есть количество дней с "1970-01-01T00:00:00".

```python
mdates.set_epoch('1970-01-01T00:00:00')
```
