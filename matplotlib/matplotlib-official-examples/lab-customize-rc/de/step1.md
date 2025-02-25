# Erstellen einer Funktion zum Festlegen von Standardparametern

Um eine Funktion zu erstellen, die die Standardparameter für Ihre Diagramme festlegt, können Sie die Methode `rcParams.update()` verwenden. Diese Methode nimmt ein Wörterbuch mit Parameternamen und -werten entgegen und aktualisiert die aktuellen Standardwerte mit den neuen. Hier ist ein Beispiel für eine Funktion, die einige Standardparameter für Veröffentlichungsdiagramme festlegt:

```python
def set_pub():
    rcParams.update({
        "font.weight": "bold",  # fette Schriftarten
        "tick.labelsize": 15,   # große Tick-Labels
        "lines.linewidth": 1,   # dicke Linien
        "lines.color": "k",     # schwarze Linien
        "grid.color": "0.5",    # graue Gitternetzlinien
        "grid.linestyle": "-",  # feste Gitternetzlinien
        "grid.linewidth": 0.5,  # dünne Gitternetzlinien
        "savefig.dpi": 300,     # Ausgabe mit höherer Auflösung.
    })
```
