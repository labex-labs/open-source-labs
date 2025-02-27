# Datenvisualisierung

In diesem Schritt werden wir die erzeugten Daten visualisieren.

```python
import matplotlib.pyplot as plt

plt.plot(X, y, label="Expected signal")
plt.legend()
plt.xlabel("X")
_ = plt.ylabel("y")
```
