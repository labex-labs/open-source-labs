# Histogramm, Legende und Titel erstellen

Zunächst werden wir das Histogramm, die Legende und den Titel mit Matplotlib erstellen. Wir werden auch jedem Objekt mithilfe der Methode `set_gid()` IDs zuweisen. Dies wird helfen, die in Python erstellten Matplotlib-Objekte mit den entsprechenden SVG-Konstrukten zu verknüpfen, die im zweiten Schritt analysiert werden.

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# Create histogram, legend, and title
plt.figure()
r = np.random.randn(100)
r1 = r + 1
labels = ['Kaninchen', 'Frösche']
H = plt.hist([r, r1], label=labels)
containers = H[-1]
leg = plt.legend(frameon=False)
plt.title("Von einem Webbrowser her können Sie auf den Legendenmarker klicken,\n"
          "um das entsprechende Histogramm an- oder auszublenden.")

# Assign IDs to the SVG objects we'll modify
hist_patches = {}
for ic, c in enumerate(containers):
    hist_patches[f'hist_{ic}'] = []
    for il, element in enumerate(c):
        element.set_gid(f'hist_{ic}_patch_{il}')
        hist_patches[f'hist_{ic}'].append(f'hist_{ic}_patch_{il}')

# Set IDs for the legend patches
for i, t in enumerate(leg.get_patches()):
    t.set_gid(f'leg_patch_{i}')

# Set IDs for the text patches
for i, t in enumerate(leg.get_texts()):
    t.set_gid(f'leg_text_{i}')
```
