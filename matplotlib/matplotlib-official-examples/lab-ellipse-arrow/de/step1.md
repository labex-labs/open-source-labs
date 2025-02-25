# Matplotlib importieren und Figur und Achse erstellen

Zunächst musst du Matplotlib importieren und eine Figur und eine Achse erstellen. Die Figur und die Achse sind die Container für deine Grafik.

```python
import matplotlib.pyplot as plt

# Erstellen Sie eine Figur und eine Achse
fig, ax = plt.subplots(subplot_kw={"aspect": "equal"})
```
