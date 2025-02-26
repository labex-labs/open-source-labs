# Übung 6.14: Generatorausdrücke in Funktionsargumenten

Generatorausdrücke werden manchmal in Funktionsargumenten eingesetzt. Es sieht zunächst ein wenig seltsam aus, aber versuchen Sie dieses Experiment:

```python
>>> nums = [1,2,3,4,5]
>>> sum([x*x for x in nums])    # Eine List Comprehension
55
>>> sum(x*x for x in nums)      # Ein Generatorausdruck
55
>>>
```

Im obigen Beispiel würde die zweite Version mit Generatoren erheblich weniger Speicher verwenden, wenn es um eine große Liste geht.

In Ihrer `portfolio.py`-Datei haben Sie einige Berechnungen mit List Comprehensions durchgeführt. Versuchen Sie, diese durch Generatorausdrücke zu ersetzen.
