# Erstellen von Teilplots für Beispielplots

Wir werden ein 3 x 3-Gitter von Teilplots erstellen, um unsere Beispielplots anzuzeigen.

```python
fig, axs = plt.subplots(
    3, 3, figsize=(9, 9), layout="constrained", gridspec_kw={"hspace": 0.1})
```
