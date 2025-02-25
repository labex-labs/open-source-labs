# Convertissez une date et heure au format Matplotlib

Maintenant que l'époque a été définie, nous pouvons convertir un objet `datetime` en une date Matplotlib en utilisant la fonction `mdates.date2num`.

```python
date1 = datetime.datetime(2000, 1, 1, 0, 10, 0, 12, tzinfo=datetime.timezone.utc)
mdate1 = mdates.date2num(date1)
```
