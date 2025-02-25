# Setzen der Epoche auf die neue Standardeinstellung

Um moderne Datumswerte mit Mikrosekundengenauigkeit zu verwenden, müssen wir die Epoche auf die neue Standardeinstellung setzen, die die Anzahl der Tage seit "1970-01-01T00:00:00" angibt.

```python
mdates.set_epoch('1970-01-01T00:00:00')
```
