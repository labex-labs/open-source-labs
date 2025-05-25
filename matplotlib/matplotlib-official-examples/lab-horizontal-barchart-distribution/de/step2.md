# Daten vorbereiten

Wir müssen die Kategorien und die Umfrageergebnisse definieren. In diesem Beispiel haben wir eine Umfrage, bei der die Menschen ihre Zustimmung zu Fragen auf einer fünfstufigen Skala bewerteten. Wir werden die Kategorien als `category_names` und die Umfrageergebnisse als `results` definieren.

```python
category_names = ['Stark 不同意', '不同意',
                  'Weder zustimmen noch ablehnen', 'Zustimmen', 'Stark zustimmen']
results = {
    'Frage 1': [10, 15, 17, 32, 26],
    'Frage 2': [26, 22, 29, 10, 13],
    'Frage 3': [35, 37, 7, 2, 19],
    'Frage 4': [32, 11, 9, 15, 33],
    'Frage 5': [21, 29, 5, 5, 40],
    'Frage 6': [8, 19, 5, 30, 38]
}
```
