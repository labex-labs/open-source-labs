# Arbeiten mit mehreren Stock-Objekten

In der objektorientierten Programmierung ist eine Klasse wie eine Blaupause, und Instanzen dieser Klasse sind die tatsächlichen Objekte, die anhand dieser Blaupause erstellt werden. Unsere `Stock`-Klasse ist eine Blaupause zur Darstellung von Aktien. Wir können mehrere Instanzen dieser `Stock`-Klasse erstellen, um verschiedene Aktien darzustellen. Jede Instanz hat ihre eigenen Attribute, wie den Aktiennamen, die Anzahl der Anteile und den Preis pro Anteil.

1. Während die Python-Sitzung im interaktiven Modus noch läuft, werden wir ein weiteres `Stock`-Objekt erstellen. Diesmal soll es IBM repräsentieren. Um eine Instanz der `Stock`-Klasse zu erstellen, rufen wir den Klassennamen wie eine Funktion auf und übergeben die erforderlichen Argumente. Die Argumente hier sind der Aktienname, die Anzahl der Anteile und der Preis pro Anteil.

```python
t = Stock('IBM', 50, 91.5)
```

In dieser Codezeile erstellen wir ein neues `Stock`-Objekt namens `t`, das IBM repräsentiert. Es hat 50 Anteile, und jeder Anteil kostet 91,5 $.

2. Jetzt möchten wir die Kosten dieser neuen Aktie berechnen. Die `Stock`-Klasse hat eine Methode namens `cost()`, die die Gesamtkosten der Aktie berechnet, indem sie die Anzahl der Anteile mit dem Preis pro Anteil multipliziert.

```python
t.cost()
```

Wenn Sie diesen Code ausführen, ruft Python die `cost()`-Methode auf dem `t`-Objekt auf und gibt die Gesamtkosten zurück.

Ausgabe:

```
4575.0
```

3. Wir können unsere Aktieninformationen auf eine schöne, organisierte Weise formatieren und anzeigen, indem wir die String-Formatierung in Python verwenden. Die String-Formatierung ermöglicht es uns, anzugeben, wie verschiedene Datentypen in einem String dargestellt werden sollen.

```python
print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
```

In diesem Code verwenden wir die alte Art der String-Formatierung in Python. Der `%`-Operator wird verwendet, um Werte in eine String-Vorlage einzufügen. Die String-Vorlage `'%10s %10d %10.2f'` definiert, wie der Aktienname, die Anzahl der Anteile und der Preis formatiert werden sollen.

Ausgabe:

```
      GOOG        100     490.10
```

Dieser formatierte String funktioniert wie folgt:

- `%10s` formatiert einen String in einem Feld mit einer Breite von 10 Zeichen (rechtsbündig). Das bedeutet, dass der Aktienname in einem Bereich von 10 Zeichen Breite platziert wird und innerhalb dieses Bereichs rechtsbündig ausgerichtet wird.
- `%10d` formatiert eine Ganzzahl in einem Feld mit einer Breite von 10 Zeichen. Die Anzahl der Anteile wird also in einem Bereich von 10 Zeichen Breite platziert.
- `%10.2f` formatiert eine Fließkommazahl mit zwei Dezimalstellen in einem Feld mit einer Breite von 10 Zeichen. Der Preis wird mit zwei Dezimalstellen angezeigt und in einem Bereich von 10 Zeichen Breite platziert.

4. Jetzt formatierten wir die IBM-Aktieninformationen auf die gleiche Weise. Wir müssen nur den Objektnamen von `s` auf `t` in der String-Formatierung ändern.

```python
print('%10s %10d %10.2f' % (t.name, t.shares, t.price))
```

Ausgabe:

```
       IBM         50      91.50
```

5. In modernem Python können wir auch f-Strings zur Formatierung verwenden. F-Strings sind lesbarer und einfacher zu verwenden. Vergleichen wir die Kosten beider Aktien mit f-Strings.

```python
print(f"Google stock costs ${s.cost()}, IBM stock costs ${t.cost()}")
```

In diesem f-String setzen wir direkt Ausdrücke in geschweifte Klammern `{}` ein. Python wertet diese Ausdrücke aus und fügt die Ergebnisse in den String ein.

Ausgabe:

```
Google stock costs $49010.0, IBM stock costs $4575.0
```

6. Wenn Sie mit Ihren Experimenten fertig sind, ist es an der Zeit, den interaktiven Python-Modus zu beenden. Sie können dies tun, indem Sie die `exit()`-Funktion verwenden.

```python
exit()
```

Jedes `Stock`-Objekt verwaltet seine eigenen Attribute, was zeigt, wie Klasseninstanzen in der objektorientierten Programmierung funktionieren. Dies ermöglicht es uns, mehrere Aktienobjekte zu erstellen, jedes mit unterschiedlichen Werten, während sie die gleichen Methoden teilen.
