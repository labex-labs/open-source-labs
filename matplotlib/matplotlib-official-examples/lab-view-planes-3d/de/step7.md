# Bezeichnung jeder primären 3D-Ansichtsebene

Wir verwenden die in Schritt 2 definierte Funktion `annotate_axes`, um jede primäre 3D-Ansichtsebene mit ihren jeweiligen Winkeln zu bezeichnen.

```python
for plane, angles in views:
    label = f'{plane}\n{angles}'
    annotate_axes(axd[plane], label, fontsize=14)
```
