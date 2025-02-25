# Matplotlib importieren und die on_close-Funktion definieren

In diesem Schritt importieren wir Matplotlib und definieren die `on_close`-Funktion, die aufgerufen wird, wenn die Figur geschlossen wird. Die Funktion wird einfach eine Nachricht in die Konsole ausgeben.

```python
import matplotlib.pyplot as plt

def on_close(event):
    print('Closed Figure!')
```
