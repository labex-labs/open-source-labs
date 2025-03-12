# Das Verständnis des Hauptmoduls (Main Module) in Python

In Python fungiert ein Skript, wenn es direkt ausgeführt wird, als "Hauptmodul" (main module). Python hat eine spezielle Variable namens `__name__`. Wenn eine Datei direkt ausgeführt wird, setzt Python den Wert von `__name__` auf `"__main__"`. Dies unterscheidet sich von dem Fall, wenn die Datei als Modul importiert wird.

Diese Eigenschaft ist sehr nützlich, da sie es Ihnen ermöglicht, Code zu schreiben, der sich je nachdem unterschiedlich verhält, ob die Datei direkt ausgeführt oder importiert wird. Beispielsweise möchten Sie möglicherweise, dass ein bestimmter Code nur ausgeführt wird, wenn Sie die Datei als Skript ausführen, nicht aber, wenn sie von einem anderen Skript importiert wird.

## Das Ändern von pcost.py zur Nutzung des Hauptmodul-Musters

Ändern wir das Programm `pcost.py`, um dieses Muster zu nutzen.

1. Zunächst müssen Sie die Datei `pcost.py` im Editor öffnen. Sie können die folgenden Befehle verwenden, um in das Projektverzeichnis zu navigieren und die Datei zu erstellen, falls sie noch nicht existiert:

```bash
cd ~/project
touch pcost.py
```

Der Befehl `cd` wechselt das aktuelle Verzeichnis in das `project`-Verzeichnis in Ihrem Home-Verzeichnis. Der Befehl `touch` erstellt eine neue Datei namens `pcost.py`, falls sie noch nicht existiert.

2. Ändern Sie nun die Datei `pcost.py` so, dass sie wie folgt aussieht:

```python
# pcost.py

def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                nshares = int(fields[1])
                price = float(fields[2])
                total_cost += nshares * price
            except (ValueError, IndexError):
                print(f"Couldn't parse: {line}")

    return total_cost

# Dieser Code wird nur ausgeführt, wenn die Datei als Skript ausgeführt wird
if __name__ == "__main__":
    total = portfolio_cost('portfolio.dat')
    print(total)
```

Die Hauptänderung besteht darin, dass wir den Code am Ende in eine `if __name__ == "__main__":`-Bedingung eingebettet haben. Dies bedeutet, dass der Code in diesem Block nur ausgeführt wird, wenn die Datei direkt als Skript ausgeführt wird, nicht wenn sie als Modul importiert wird.

3. Speichern Sie die Datei nach diesen Änderungen und verlassen Sie den Editor.

## Das Testen des geänderten Moduls

Testen wir nun unser geändertes Modul auf zwei verschiedene Arten, um zu sehen, wie es sich verhält.

1. Führen Sie zunächst das Programm direkt als Skript mit dem folgenden Befehl aus:

```bash
python3 pcost.py
```

Sie sollten die Ausgabe `44671.15` sehen, genau wie zuvor. Dies liegt daran, dass wenn Sie das Skript direkt ausführen, die Variable `__name__` auf `"__main__"` gesetzt wird, sodass der Code im `if __name__ == "__main__":`-Block ausgeführt wird.

2. Starten Sie als Nächstes erneut den Python-Interpreter und importieren Sie das Modul:

```bash
python3
```

```python
import pcost
```

Diesmal sollten Sie keine Ausgabe sehen. Wenn Sie das Modul importieren, wird die Variable `__name__` auf `"pcost"` (der Modulname) gesetzt, nicht auf `"__main__"`. Daher wird der Code im `if __name__ == "__main__":`-Block nicht ausgeführt.

3. Um zu überprüfen, ob die Funktion `portfolio_cost` weiterhin funktioniert, können Sie sie wie folgt aufrufen:

```python
pcost.portfolio_cost('portfolio.dat')
```

Die Funktion sollte `44671.15` zurückgeben, was bedeutet, dass sie korrekt funktioniert.

4. Beenden Sie schließlich den Python-Interpreter mit dem folgenden Befehl:

```python
exit()
```

Dieses Muster ist sehr nützlich, wenn Sie Python-Dateien erstellen, die sowohl als importierbare Module als auch als eigenständige Skripte verwendet werden können. Der Code im `if __name__ == "__main__":`-Block wird nur ausgeführt, wenn die Datei direkt ausgeführt wird, nicht wenn sie als Modul importiert wird.
