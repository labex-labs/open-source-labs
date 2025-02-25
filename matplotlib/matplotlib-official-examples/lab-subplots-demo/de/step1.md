# Erstellen einer Abbildung mit einem einzelnen Subplot

Der einfachste Weg, einen einzelnen Subplot zu erstellen, ist die Verwendung der Funktion `subplots()` ohne zusätzliche Argumente. Diese Funktion gibt ein `Figure`-Objekt und ein einzelnes `Axes`-Objekt zurück.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

```
