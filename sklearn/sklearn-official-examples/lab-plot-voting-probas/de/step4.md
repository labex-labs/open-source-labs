# Holen Sie sich die Klasswahrscheinlichkeiten für die erste Probe in der Datenmenge

Wir werden die Klasswahrscheinlichkeiten für die erste Probe in der Datenmenge abrufen und sie in class1_1 und class2_1 speichern.

```python
class1_1 = [pr[0, 0] for pr in probas]
class2_1 = [pr[0, 1] for pr in probas]
```
