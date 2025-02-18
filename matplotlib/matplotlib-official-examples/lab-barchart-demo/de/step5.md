# Definieren der Daten für das Diagramm

Wir definieren die Daten für das Diagramm mithilfe der zuvor definierten benannten Tupel (named tuples). Wir erstellen ein `Student`-Tupel für Johnny Doe und ein Wörterbuch mit `Score`-Tupeln für jeden Test.

```python
student = Student(name='Johnny Doe', grade=2, gender='Boy')
scores_by_test = {
    'Pacer Test': Score(7, 'laps', percentile=37),
    'Flexed Arm\n Hang': Score(48, 'sec', percentile=95),
    'Mile Run': Score('12:52', 'min:sec', percentile=73),
    'Agility': Score(17, 'sec', percentile=60),
    'Push Ups': Score(14, '', percentile=16),
}
```
