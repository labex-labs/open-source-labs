# Zuweisungsbeispiel

Betrachten Sie diesen Codeausschnitt.

```python
a = [1,2,3]
b = a
c = [a,b]
```

Ein Diagramm der zugrunde liegenden Arbeitsspeicheroperationen. In diesem Beispiel gibt es nur ein Listenobjekt `[1,2,3]`, aber vier unterschiedliche Referenzen darauf.

![Memory reference diagram example](../assets/references.png)

Dies bedeutet, dass das Ändern eines Werts alle Referenzen _beeinflusst_.

```python
>>> a.append(999)
>>> a
[1,2,3,999]
>>> b
[1,2,3,999]
>>> c
[[1,2,3,999], [1,2,3,999]]
>>>
```

Bemerken Sie, wie eine Änderung in der ursprünglichen Liste überall sonst sichtbar wird (auweia!). Dies liegt daran, dass keine Kopien gemacht wurden. Alles verweist auf das gleiche Objekt.
