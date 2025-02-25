# Zahl in Bereich abbilden

Schreiben Sie eine Funktion namens `num_to_range`, die fünf Argumente akzeptiert: `num`, `inMin`, `inMax`, `outMin` und `outMax`. Die Funktion sollte `num` im Bereich von `outMin` - `outMax` abbilden, ausgehend von `inMin` - `inMax`. Mit anderen Worten, die Funktion sollte eine Zahl (`num`), die innerhalb eines bestimmten Bereichs (`inMin` - `inMax`) liegt, in einen neuen Bereich (`outMin` - `outMax`) abbilden.

```python
def num_to_range(num, inMin, inMax, outMin, outMax):
  return outMin + (float(num - inMin) / float(inMax - inMin) * (outMax
                  - outMin))
```

```python
num_to_range(5, 0, 10, 0, 100) # 50.0
```
