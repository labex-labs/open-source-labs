# Matplotlib importieren

Bevor wir mit der Annotation von Graphen mit Matplotlib beginnen können, müssen wir zunächst die Bibliothek importieren. In diesem Schritt importieren wir Matplotlib und erstellen einen einfachen Graphen, den wir für die Annotation verwenden werden.

```python
import matplotlib.pyplot as plt

# Create a simple plot
fig, ax = plt.subplots()
ax.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.show()
```
