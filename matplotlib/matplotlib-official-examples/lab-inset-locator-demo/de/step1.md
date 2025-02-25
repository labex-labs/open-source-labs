# Erstellen eines Diagramms mit zwei Unterdiagrammen

Zunächst müssen wir ein Diagramm mit zwei Unterdiagrammen erstellen. Wir werden die `plt.subplots()`-Methode verwenden, um ein Diagramm mit zwei nebeneinander liegenden Unterdiagrammen zu erstellen.

```python
import matplotlib.pyplot as plt

fig, (ax, ax2) = plt.subplots(1, 2, figsize=[5.5, 2.8])
```
