# Legende für bestimmte Linien erstellen

In diesem Schritt werden wir eine Legende für bestimmte Linien erstellen.

```python
# Import notwendige Bibliotheken
import matplotlib.pyplot as plt
import numpy as np

# Definiere Daten für das Diagramm
t1 = np.arange(0.0, 2.0, 0.1)
t2 = np.arange(0.0, 2.0, 0.01)

# Erstelle ein Diagramm mit mehreren Linien
fig, ax = plt.subplots()
l1, = ax.plot(t2, np.exp(-t2))
l2, l3 = ax.plot(t2, np.sin(2 * np.pi * t2), '--o', t1, np.log(1 + t1), '.')
l4, = ax.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2),'s-.')

# Erstelle eine Legende für zwei der Linien
ax.legend((l2, l4), ('oszillierend', 'gedämpft'), loc='upper right', shadow=True)

# Füge Beschriftungen und Titel zum Diagramm hinzu
ax.set_xlabel('Zeit')
ax.set_ylabel('Spannung')
ax.set_title('Gedämpfte Schwingung')

# Zeige das Diagramm an
plt.show()
```
