# Definieren einer Methode zum Anpassen der Achsenkantenpositionen

In diesem Schritt definieren wir eine Methode, die die Position der Achsenkanten basierend auf den angegebenen Achsenkantenpositionen anpasst.

```python
def adjust_spines(ax, spines):
    """
    Anpasst die Position der Achsenkanten basierend auf den angegebenen Achsenkantenpositionen.

    Parameter:
        ax (Axes): Das Matplotlib-Axes-Objekt, für das die Achsenkanten angepasst werden sollen.
        spines (Liste von str): Die gewünschten Achsenkantenpositionen. Gültige Optionen sind 'left' (links), 'right' (rechts), 'top' (oben), 'bottom' (unten).

    Rückgabe:
        None
    """
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', 10))  # verschiebt die Achsenkante um 10 Punkte nach außen
        else:
            spine.set_color('none')  # zeichnet die Achsenkante nicht

    # deaktiviert die Striche an Stellen, wo keine Achsenkante ist
    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
    else:
        ax.yaxis.set_ticks([])

    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')
    else:
        ax.xaxis.set_ticks([])
```
