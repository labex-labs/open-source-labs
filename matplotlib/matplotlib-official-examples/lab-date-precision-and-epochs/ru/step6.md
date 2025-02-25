# Преобразовать datetime в дату Matplotlib с новой эпохой

Теперь, когда эпоху установлено по новому умолчанию, мы можем преобразовать объект `datetime` в дату Matplotlib с использованием функции `mdates.date2num`.

```python
date1 = datetime.datetime(2020, 1, 1, 0, 10, 0, 12, tzinfo=datetime.timezone.utc)
mdate1 = mdates.date2num(date1)
```
