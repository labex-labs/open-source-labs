# Das Verständnis von Python-Modulen

In Python ist ein Modul (module) wie ein Behälter, der Python-Definitionen und -Anweisungen enthält. Es ist im Wesentlichen eine Datei, und der Name dieser Datei ist der Modulname mit der Erweiterung `.py` am Ende. Stellen Sie sich Module als Werkzeugkästen vor. Sie helfen Ihnen, Ihren Python-Code auf logische Weise zu organisieren, was die Wiederverwendung und Wartung erleichtert. Genauso wie Sie verschiedene Werkzeuge in separaten Kästen aufbewahren würden, um die Organisation zu verbessern, können Sie verwandten Python-Code in verschiedene Module gruppieren.

Schauen wir uns die Dateien an, die für dieses Lab eingerichtet wurden:

1. Zunächst öffnen wir die Datei `stock.py` im Editor, um zu sehen, was darin enthalten ist. Dazu verwenden wir die folgenden Befehle. Der Befehl `cd` wechselt in das Verzeichnis `project`, in dem sich unsere Datei befindet, und der Befehl `cat` zeigt den Inhalt der Datei an.

```bash
cd ~/project
cat stock.py
```

Diese Datei `stock.py` definiert eine Klasse `Stock`. Eine Klasse ist wie ein Bauplan zum Erstellen von Objekten. In diesem Fall repräsentiert die Klasse `Stock` eine Aktie. Sie hat Attribute (die wie Eigenschaften sind) für den Namen der Aktie, die Anzahl der Anteile und den Preis. Sie hat auch eine Methode (die wie eine Funktion im Zusammenhang mit der Klasse ist), um die Kosten der Aktie zu berechnen.

2. Als Nächstes untersuchen wir die Datei `pcost.py`. Wir verwenden erneut den Befehl `cat`, um ihren Inhalt anzuzeigen.

```bash
cat pcost.py
```

Diese Datei definiert eine Funktion namens `portfolio_cost()`. Eine Funktion ist ein Codeblock, der eine bestimmte Aufgabe ausführt. Die Funktion `portfolio_cost()` liest eine Portfolio-Datei und berechnet die Gesamtkosten aller Aktien in diesem Portfolio.

3. Jetzt schauen wir uns die Beispiel-Portfolio-Daten an. Wir verwenden den Befehl `cat`, um den Inhalt der Datei `portfolio.dat` anzuzeigen.

```bash
cat portfolio.dat
```

Diese Datei enthält Aktiendaten in einem einfachen Format. Jede Zeile enthält das Tickersymbol der Aktie, die Anzahl der Anteile und den Preis pro Anteil.

## Die Verwendung der import-Anweisung

Python's `import`-Anweisung ist ein leistungsstarkes Werkzeug, das es Ihnen ermöglicht, Code aus anderen Modulen in Ihrem aktuellen Programm zu verwenden. Es ist wie das Ausleihen von Werkzeugen aus anderen Werkzeugkästen. Üben wir verschiedene Arten, Code zu importieren:

1. Zunächst müssen wir den Python-Interpreter starten. Der Python-Interpreter ist ein Programm, das Python-Code ausführt. Wir verwenden den folgenden Befehl, um ihn zu starten.

```bash
python3
```

2. Jetzt importieren wir das Modul `pcost` und sehen, was passiert. Wenn wir die `import`-Anweisung verwenden, sucht Python nach der Datei `pcost.py` und macht den darin enthaltenen Code für uns verfügbar.

```python
import pcost
```

Sie sollten die Ausgabe `44671.15` sehen. Dies sind die berechneten Kosten des Portfolios aus der Datei `portfolio.dat`. Wenn das Modul `pcost` importiert wird, wird der Code am Ende der Datei `pcost.py` automatisch ausgeführt.

3. Versuchen wir, die Funktion `portfolio_cost()` mit einer anderen Portfolio-Datei aufzurufen. Wir verwenden die Syntax `pcost.portfolio_cost()`, um die Funktion aus dem Modul `pcost` aufzurufen.

```python
pcost.portfolio_cost('portfolio2.dat')
```

Die Ausgabe sollte `19908.75` sein, was die Gesamtkosten der Aktien in der zweiten Portfolio-Datei darstellt.

4. Jetzt importieren wir eine bestimmte Klasse aus dem Modul `stock`. Anstatt das gesamte Modul zu importieren, können wir einfach die Klasse `Stock` mit der `from...import`-Anweisung importieren.

```python
from stock import Stock
```

5. Nachdem wir die Klasse `Stock` importiert haben, können wir ein `Stock`-Objekt erstellen. Ein Objekt ist eine Instanz einer Klasse. Wir erstellen ein `Stock`-Objekt mit dem Namen `GOOG`, 100 Anteilen und einem Preis von `490.10`. Dann geben wir den Namen der Aktie aus und berechnen ihre Kosten mit der Methode `cost()`.

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)
print(s.cost())
```

Die Ausgabe sollte sein:

```
GOOG
49010.0
```

6. Schließlich können wir, wenn wir mit der Verwendung des Python-Interpreters fertig sind, ihn mit der Funktion `exit()` beenden.

```python
exit()
```

Dieses Lab hat zwei verschiedene Arten gezeigt, Python-Code zu importieren:

- `import module_name` - Dies importiert das gesamte Modul und macht alle Funktionen, Klassen und Variablen in diesem Modul verfügbar.
- `from module_name import specific_item` - Dies importiert nur ein bestimmtes Element (wie eine Klasse oder eine Funktion) aus dem Modul, was nützlich sein kann, wenn Sie nur einen Teil der Funktionalität des Moduls benötigen.
