# Wörterbuchkonstruktion

Beispiel für das Erstellen eines Wörterbuchs von Grund auf.

```python
prices = {} # Initiales leeres Wörterbuch

# Fügen Sie neue Elemente hinzu
prices['GOOG'] = 513.25
prices['CAT'] = 87.22
prices['IBM'] = 93.37
```

Ein Beispiel für das Befüllen des Wörterbuchs aus den Inhalten einer Datei.

```python
prices = {} # Initiales leeres Wörterbuch

with open('prices.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        prices[row[0]] = float(row[1])
```

Hinweis: Wenn Sie das auf die `prices.csv`-Datei ausprobieren, werden Sie feststellen, dass es fast funktioniert - am Ende gibt es eine leere Zeile, die dazu führt, dass das Programm abstürzt. Sie müssen eine Möglichkeit finden, den Code zu modifizieren, um dies zu berücksichtigen (siehe Übung 2.6).
