# Einlesen von Daten aus einer Excel-Datei

Das Einlesen von Daten aus einer Excel-Datei ist genauso einfach wie das Einlesen von Daten aus einer CSV-Datei. Wir werden die `read_excel`-Funktion aus pandas verwenden.

```python
# Reading data from an Excel file
titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
```
