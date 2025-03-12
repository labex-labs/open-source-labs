# Verständnis der Speicherzuweisung von Listen

In Python sind Listen eine sehr nützliche Datenstruktur, insbesondere wenn Sie Elemente hinzufügen müssen. Python - Listen sind so konzipiert, dass Anhängeeffizient sind. Anstatt genau die benötigte Speichermenge zuzuweisen, weist Python zusätzlichen Speicher im Voraus für zukünftige Hinzufügungen zu. Diese Strategie minimiert die Anzahl der erforderlichen Speicherumzuweisungen, wenn die Liste wächst.

Lassen Sie uns dieses Konzept besser verstehen, indem wir die Funktion `sys.getsizeof()` verwenden. Diese Funktion gibt die Größe eines Objekts in Bytes zurück, was uns hilft, zu sehen, wie viel Speicher eine Liste in verschiedenen Stadien verwendet.

1. Zunächst müssen Sie in Ihrem Terminal eine interaktive Python - Shell öffnen. Dies ist wie ein Spielplatz, auf dem Sie sofort Python - Code ausführen können. Um sie zu öffnen, geben Sie den folgenden Befehl in Ihrem Terminal ein und drücken Sie die Eingabetaste:

```bash
python3
```

2. Sobald Sie in der interaktiven Python - Shell sind, müssen Sie das Modul `sys` importieren. Module in Python sind wie Werkzeugkästen, die nützliche Funktionen enthalten. Das Modul `sys` hat die von uns benötigte Funktion `getsizeof()`. Nach dem Importieren des Moduls erstellen Sie eine leere Liste namens `items`. Hier ist der Code dafür:

```python
import sys
items = []
```

3. Jetzt überprüfen wir die anfängliche Größe der leeren Liste. Wir verwenden die Funktion `sys.getsizeof()` mit der Liste `items` als Argument. Geben Sie den folgenden Code in der interaktiven Python - Shell ein und drücken Sie die Eingabetaste:

```python
sys.getsizeof(items)
```

Sie sollten einen Wert wie `64` Bytes sehen. Dieser Wert repräsentiert die Overhead - Kosten für eine leere Liste. Die Overhead - Kosten sind die grundlegende Speichermenge, die Python verwendet, um die Liste zu verwalten, auch wenn sie keine Elemente enthält.

4. Als Nächstes fügen wir der Liste nacheinander Elemente hinzu und beobachten, wie sich die Speicherzuweisung ändert. Wir verwenden die Methode `append()`, um ein Element zur Liste hinzuzufügen, und überprüfen dann erneut die Größe. Hier ist der Code:

```python
items.append(1)
sys.getsizeof(items)
```

Sie sollten einen größeren Wert, etwa `96` Bytes, sehen. Diese Größenzunahme zeigt, dass Python mehr Speicher zugewiesen hat, um das neue Element aufzunehmen.

5. Lassen Sie uns weiterhin mehr Elemente zur Liste hinzufügen und die Größe nach jeder Hinzufügung überprüfen. Hier ist der Code dafür:

```python
items.append(2)
sys.getsizeof(items)  # Größe bleibt gleich

items.append(3)
sys.getsizeof(items)  # Größe bleibt weiterhin unverändert

items.append(4)
sys.getsizeof(items)  # Größe bleibt weiterhin unverändert

items.append(5)
sys.getsizeof(items)  # Größe springt auf einen größeren Wert
```

Sie werden feststellen, dass die Größe nicht bei jeder Anhängeoperation zunimmt. Stattdessen springt sie periodisch auf einen höheren Wert. Dies zeigt, dass Python Speicher in Blöcken zuweist, anstatt für jedes neue Element individuell.

Dieses Verhalten ist beabsichtigt. Python weist zunächst mehr Speicher zu, als benötigt wird, um häufige Umzuweisungen zu vermeiden, wenn die Liste wächst. Jedes Mal, wenn die Liste ihre aktuelle Kapazität überschreitet, weist Python einen größeren Speicherblock zu.

Denken Sie daran, dass eine Liste Verweise auf Objekte speichert, nicht die Objekte selbst. Auf einem 64 - Bit - System benötigt jeder Verweis typischerweise 8 Bytes Speicher. Dies ist wichtig zu verstehen, da es daraufhinwirkt, wie viel Speicher eine Liste tatsächlich verwendet, wenn sie verschiedene Objekttypen enthält.
