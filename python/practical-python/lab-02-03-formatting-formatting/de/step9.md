# Übung 2.11: Hinzufügen von Kopfzeilen

Angenommen, Sie hätten ein Tupel mit Kopfzeilennamen wie dieses:

```python
headers = ('Name', 'Anteile', 'Preis', 'Änderung')
```

Fügen Sie Code zu Ihrem Programm hinzu, der das obige Tupel von Kopfzeilen verwendet und eine Zeichenkette erstellt, in der jeder Kopfzeilename rechtsbündig in einem 10-zeichenweiten Feld platziert ist und jedes Feld durch ein einzelnes Leerzeichen getrennt ist.

```python
'      Name     Anteile      Preis      Änderung'
```

Schreiben Sie Code, der die Kopfzeilen verwendet und die Trennzeichenkette zwischen den Kopfzeilen und den folgenden Daten erstellt. Diese Zeichenkette besteht einfach aus einer Reihe von "-"-Zeichen unter jedem Feldnamen. Beispielsweise:

```python
'---------- ---------- ---------- -----------'
```

Wenn Sie fertig sind, sollte Ihr Programm die Tabelle ausgeben, die am Anfang dieser Übung gezeigt wird.

          Name     Anteile      Preis     Änderung
    ---------- ---------- ---------- ----------
            AA        100       9.22     -22.98
           IBM         50     106.28      15.18
           CAT        150      35.46     -47.98
          MSFT        200      20.89     -30.34
            GE         95      13.48     -26.89
          MSFT         50      20.89     -44.21
           IBM        100     106.28      35.84
