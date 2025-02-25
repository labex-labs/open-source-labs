# Importieren der erforderlichen Bibliotheken und Erstellen einer Figur mit Teilplots

Wir beginnen, indem wir die erforderlichen Bibliotheken importieren und eine Figur mit Teilplots erstellen.

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
```
