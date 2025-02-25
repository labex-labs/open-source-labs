# Zufällige Daten generieren

Zunächst müssen wir 100 zufällige Datensätze generieren, wobei jeder Datensatz 1000 Zufallszahlen zwischen 0 und 1 enthält. Wir werden das Zufallsmodul von numpy verwenden, um die zufälligen Daten zu generieren.

```python
import numpy as np

np.random.seed(19680801)

X = np.random.rand(100, 1000)
```
