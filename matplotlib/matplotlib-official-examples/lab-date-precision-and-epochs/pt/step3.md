# Converter datetime para data do matplotlib

Agora que a época foi definida, podemos converter um objeto `datetime` para uma data do Matplotlib usando a função `mdates.date2num`.

```python
date1 = datetime.datetime(2000, 1, 1, 0, 10, 0, 12, tzinfo=datetime.timezone.utc)
mdate1 = mdates.date2num(date1)
```
