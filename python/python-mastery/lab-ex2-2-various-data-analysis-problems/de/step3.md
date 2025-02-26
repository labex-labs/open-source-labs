# Collections

Das `collections`-Modul hat eine Vielzahl von Klassen für eine spezialisiertere Datenmanipulation. Beispielsweise kann das letzte Beispiel mit einem `Counter` wie folgt gelöst werden:

```python
>>> from collections import Counter
>>> totals = Counter()
>>> for s in portfolio:
        totals[s['name']] += s['shares']

>>> totals
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>>
```

Counter sind interessant, da sie andere Arten von Operationen wie Rangfolge und Mathematik unterstützen. Beispielsweise:

```python
>>> # Holen Sie sich die zwei häufigsten Positionen
>>> totals.most_common(2)
[('MSFT', 250), ('IBM', 150)]
>>>

>>> # Zusammenfügen von Countern
>>> more = Counter()
>>> more['IBM'] = 75
>>> more['AA'] = 200
>>> more['ACME'] = 30
>>> more
Counter({'AA': 200, 'IBM': 75, 'ACME': 30})
>>> totals
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>> totals + more
Counter({'AA': 300, 'MSFT': 250, 'IBM': 225, 'CAT': 150, 'GE': 95, 'ACME': 30})
>>>
```

Das `defaultdict`-Objekt kann verwendet werden, um Daten zu gruppieren. Beispielsweise möchten Sie es einfacher machen, alle passenden Einträge für einen gegebenen Namen wie IBM zu finden. Probieren Sie dies:

```python
>>> from collections import defaultdict
>>> byname = defaultdict(list)
>>> for s in portfolio:
        byname[s['name']].append(s)

>>> byname['IBM']
[{'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'IBM','shares': 100, 'price': 70.44}]
>>> byname['AA']
[{'name': 'AA','shares': 100, 'price': 32.2}]
>>>
```

Das Schlüsselmerkmal, das dies ermöglicht, ist, dass ein `defaultdict` automatisch Elemente für Sie initialisiert - was das Einfügen eines neuen Elements und einen `append()`-Vorgang zusammen kombiniert.
