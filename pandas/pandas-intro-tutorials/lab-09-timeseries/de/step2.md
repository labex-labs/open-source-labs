# Umwandeln von Zeichenfolgen in Datumszeitobjekte

Die Daten im Spalten "datetime" sind derzeit Zeichenfolgen. Wir möchten diese in Datumszeitobjekte umwandeln, um eine einfachere Manipulation zu ermöglichen.

```python
# convert "datetime" column to datetime objects
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])
```
