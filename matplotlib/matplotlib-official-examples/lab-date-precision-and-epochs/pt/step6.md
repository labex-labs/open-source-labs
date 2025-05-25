# Converter datetime para data matplotlib com nova época

Agora que a época foi definida para o novo padrão, podemos converter um objeto `datetime` para uma data Matplotlib usando a função `mdates.date2num`.

```python
date1 = datetime.datetime(2020, 1, 1, 0, 10, 0, 12, tzinfo=datetime.timezone.utc)
mdate1 = mdates.date2num(date1)
```
