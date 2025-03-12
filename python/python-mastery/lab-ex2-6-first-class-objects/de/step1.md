# Das Verständnis von First-Class-Objekten in Python

In Python wird alles als Objekt behandelt. Dies umfasst auch Funktionen und Typen. Was bedeutet das? Nun, es bedeutet, dass Sie Funktionen und Typen in Datenstrukturen speichern, sie als Argumente an andere Funktionen übergeben und sogar von anderen Funktionen zurückgeben können. Dies ist ein sehr mächtiges Konzept, und wir werden es anhand der Verarbeitung von CSV-Daten als Beispiel untersuchen.

## Die Erkundung von First-Class-Typen

Zunächst starten wir den Python-Interpreter. Öffnen Sie ein neues Terminal in der WebIDE und geben Sie den folgenden Befehl ein. Dieser Befehl startet den Python-Interpreter, in dem wir unseren Python-Code ausführen werden.

```bash
python3
```

Wenn Sie in Python mit CSV-Dateien arbeiten, müssen Sie oft die Zeichenketten, die Sie aus diesen Dateien lesen, in die entsprechenden Datentypen umwandeln. Beispielsweise kann eine Zahl in einer CSV-Datei als Zeichenkette gelesen werden, aber wir möchten sie in unserem Python-Code als Ganzzahl oder Fließkommazahl verwenden. Um dies zu tun, können wir eine Liste von Konvertierungsfunktionen erstellen.

```python
coltypes = [str, int, float]
```

Beachten Sie, dass wir eine Liste erstellen, die die eigentlichen Typfunktionen enthält, nicht Zeichenketten. In Python sind Typen First-Class-Objekte, was bedeutet, dass wir sie wie jedes andere Objekt behandeln können. Wir können sie in Listen packen, herumreichen und in unserem Code verwenden.

Nun lesen wir einige Daten aus einer Portfolio-CSV-Datei, um zu sehen, wie wir diese Konvertierungsfunktionen verwenden können.

```python
import csv
f = open('portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
print(row)
```

Wenn Sie diesen Code ausführen, sollten Sie eine Ausgabe ähnlich der folgenden sehen. Dies ist die erste Datenzeile aus der CSV-Datei, dargestellt als Liste von Zeichenketten.

```
['AA', '100', '32.20']
```

Als Nächstes verwenden wir die `zip`-Funktion. Die `zip`-Funktion nimmt mehrere Iterierbare (wie Listen oder Tupel) und paart ihre Elemente. Wir werden sie verwenden, um jeden Wert aus der Zeile mit seiner entsprechenden Typkonvertierungsfunktion zu paaren.

```python
r = list(zip(coltypes, row))
print(r)
```

Dies wird die folgende Ausgabe produzieren. Jedes Paar enthält eine Typfunktion und einen Zeichenkettenwert aus der CSV-Datei.

```
[(<class 'str'>, 'AA'), (<class 'int'>, '100'), (<class 'float'>, '32.20')]
```

Jetzt, da wir diese Paare haben, können wir jede Funktion anwenden, um die Werte in ihre entsprechenden Typen umzuwandeln.

```python
record = [func(val) for func, val in zip(coltypes, row)]
print(record)
```

Die Ausgabe wird zeigen, dass die Werte in ihre entsprechenden Typen umgewandelt wurden. Die Zeichenkette 'AA' bleibt eine Zeichenkette, '100' wird zur Ganzzahl 100 und '32.20' wird zur Fließkommazahl 32.2.

```
['AA', 100, 32.2]
```

Wir können diese Werte auch mit ihren Spaltennamen kombinieren, um ein Wörterbuch zu erstellen. Ein Wörterbuch ist eine nützliche Datenstruktur in Python, die es uns ermöglicht, Schlüssel-Wert-Paare zu speichern.

```python
record_dict = dict(zip(headers, record))
print(record_dict)
```

Die Ausgabe wird ein Wörterbuch sein, in dem die Schlüssel die Spaltennamen und die Werte die konvertierten Daten sind.

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

Sie können all diese Schritte in einer einzigen Komprehension ausführen. Eine Komprehension ist eine kompakte Möglichkeit, Listen, Wörterbücher oder Mengen in Python zu erstellen.

```python
result = {name: func(val) for name, func, val in zip(headers, coltypes, row)}
print(result)
```

Die Ausgabe wird dasselbe Wörterbuch wie zuvor sein.

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

Wenn Sie mit der Arbeit im Python-Interpreter fertig sind, können Sie ihn beenden, indem Sie den folgenden Befehl eingeben.

```python
exit()
```

Diese Demonstration zeigt, wie die Behandlung von Funktionen als First-Class-Objekte in Python leistungsstarke Datenverarbeitungstechniken ermöglicht. Indem wir Typen und Funktionen als Objekte behandeln können, können wir flexibleres und kompakteres Code schreiben.
