# Convertissez `numpy.datetime64` en date Matplotlib

Les objets `numpy.datetime64` ont une précision de microseconde pour un espace temporel beaucoup plus large que les objets `.datetime`. Cependant, actuellement, le temps Matplotlib n'est converti que de nouveau en objets datetime, qui ont une résolution de microseconde et des années qui ne s'étendent que de 0000 à 9999.

```python
date1 = np.datetime64('2000-01-01T00:10:00.000012')
mdate1 = mdates.date2num(date1)
```
