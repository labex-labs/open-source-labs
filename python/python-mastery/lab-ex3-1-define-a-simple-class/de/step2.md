# Ein Portfolio lesen

Fügen Sie der Datei `stock.py` eine Funktion `read_portfolio()` hinzu, die die Daten eines Portfolios aus einer Datei in eine Liste von `Stock`-Objekten einliest. So soll es funktionieren:

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> for s in portfolio:
        print(s)

<__main__.Stock object at 0x3902f0>
<__main__.Stock object at 0x390270>
<__main__.Stock object at 0x390330>
<__main__.Stock object at 0x390370>
<__main__.Stock object at 0x3903b0>
<__main__.Stock object at 0x3903f0>
<__main__.Stock object at 0x390430>
>>>
```

Sie haben bereits eine ähnliche Funktion als Teil von Übungsblatt 2.3 geschrieben. Design-Diskussion: Soll `read_portfolio()` eine separate Funktion oder Teil der Klassendefinition sein?

## Hinweis:

Fügen Sie die Funktion `read_portfolio()` in die Datei `stock.py` hinzu.
