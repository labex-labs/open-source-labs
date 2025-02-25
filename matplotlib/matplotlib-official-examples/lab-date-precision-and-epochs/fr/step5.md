# Fixez l'époque à la nouvelle valeur par défaut

Pour utiliser des dates modernes avec une précision de microsecondes, nous devons fixer l'époque à la nouvelle valeur par défaut, qui est le nombre de jours depuis "1970-01-01T00:00:00".

```python
mdates.set_epoch('1970-01-01T00:00:00')
```
