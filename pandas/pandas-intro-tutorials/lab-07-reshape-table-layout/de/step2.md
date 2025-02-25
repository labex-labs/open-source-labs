# Tabellenzeilen sortieren

Sortieren Sie den Titanic-Datensatz nach dem Alter der Passagiere und anschließend nach der Kabinenklasse und dem Alter in absteigender Reihenfolge.

```python
# Sortieren nach Alter
titanic.sort_values(by="Age").head()

# Sortieren nach Pclass und Alter in absteigender Reihenfolge
titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head()
```
