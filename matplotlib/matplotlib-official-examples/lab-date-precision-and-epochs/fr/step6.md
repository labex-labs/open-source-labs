# Convertissez une date et heure au format Matplotlib avec la nouvelle époque

Maintenant que l'époque a été définie à la nouvelle valeur par défaut, nous pouvons convertir un objet `datetime` en une date Matplotlib en utilisant la fonction `mdates.date2num`.

```python
date1 = datetime.datetime(2020, 1, 1, 0, 10, 0, 12, tzinfo=datetime.timezone.utc)
mdate1 = mdates.date2num(date1)
```
