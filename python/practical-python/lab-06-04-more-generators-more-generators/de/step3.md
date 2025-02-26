# `itertools`-Modul

Das `itertools` ist ein Bibliotheksmodul mit verschiedenen Funktionen, die dazu dienen, Iterierer/Generatoren zu unterstützen.

```python
itertools.chain(s1,s2)
itertools.count(n)
itertools.cycle(s)
itertools.dropwhile(predicate, s)
itertools.groupby(s)
itertools.ifilter(predicate, s)
itertools.imap(function, s1,... sN)
itertools.repeat(s, n)
itertools.tee(s, ncopies)
itertools.izip(s1,..., sN)
```

Alle Funktionen verarbeiten die Daten iterativ. Sie implementieren verschiedene Arten von Iterationsmustern.

Weitere Informationen finden Sie im Tutorial [Generator Tricks for Systems Programmers](http://www.dabeaz.com/generators/) von PyCon '08.

In den vorherigen Übungen haben Sie Code geschrieben, der Zeilen verfolgte, die in eine Logdatei geschrieben wurden, und diese in eine Reihe von Zeilen analysierte. In dieser Übung bauen wir darauf fort. Stellen Sie sicher, dass `stocksim.py` weiterhin läuft.
