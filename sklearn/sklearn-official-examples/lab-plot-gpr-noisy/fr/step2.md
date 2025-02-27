# Visualisation des données

Dans cette étape, nous allons visualiser les données générées.

```python
import matplotlib.pyplot as plt

plt.plot(X, y, label="Expected signal")
plt.legend()
plt.xlabel("X")
_ = plt.ylabel("y")
```
