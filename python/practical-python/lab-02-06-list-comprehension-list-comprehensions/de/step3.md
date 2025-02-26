# Anwendungsfälle

Listenverständnisse sind äußerst nützlich. Beispielsweise können Sie die Werte eines bestimmten Dictionary-Felds sammeln:

```python
stocknames = [s['name'] for s in stocks]
```

Sie können auf Sequenzen vergleichbare Abfragen wie in einer Datenbank durchführen.

```python
a = [s for s in stocks if s['price'] > 100 und s['shares'] > 50 ]
```

Sie können auch ein Listenverständnis mit einer Sequenzreduzierung kombinieren:

```python
cost = sum([s['shares']*s['price'] for s in stocks])
```
