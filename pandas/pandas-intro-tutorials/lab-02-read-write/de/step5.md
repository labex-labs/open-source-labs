# Schreiben von Daten in eine Excel-Datei

Sie können auch die Daten in eine Excel-Datei schreiben, indem Sie die `to_excel`-Methode verwenden. Speichern wir unseren DataFrame in einer Excel-Datei.

```python
# Saving DataFrame to an Excel file
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
```
