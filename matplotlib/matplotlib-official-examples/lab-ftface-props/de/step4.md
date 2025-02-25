# Drucke zusätzliche Schriftarteigenschaften

In diesem Schritt werden wir zusätzliche Schriftarteigenschaften ausdrucken, die nur verfügbar sind, wenn das Gesicht skalierbar ist.

```python
if font.scalable:
    # die globale Begrenzung des Gesichts (xmin, ymin, xmax, ymax)
    print('Bbox:               ', font.bbox)
    # Anzahl der Schriftarteinheiten, die von der EM abgedeckt werden
    print('EM:                 ', font.units_per_EM)
    # der Aufsteiger in 26,6 Einheiten
    print('Ascender:           ', font.ascender)
    # der Absteiger in 26,6 Einheiten
    print('Descender:          ', font.descender)
    # die Höhe in 26,6 Einheiten
    print('Height:             ', font.height)
    # maximale horizontale Cursor-Vorwärtsschritt
    print('Max adv width:      ', font.max_advance_width)
    # dasselbe für die vertikale Layoutierung
    print('Max adv height:     ', font.max_advance_height)
    # vertikale Position der Unterstreichung
    print('Underline pos:      ', font.underline_position)
    # vertikale Dicke der Unterstreichung
    print('Underline thickness:', font.underline_thickness)
```
