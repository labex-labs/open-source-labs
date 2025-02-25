# Steuern der Position und Größe von Einfügebereichen

Wir können die Parameter `bbox_to_anchor` und `bbox_transform` verwenden, um die Position und Größe des Einfügebereichs zu steuern. Diese Parameter ermöglichen eine feingranulare Steuerung über die Position und Größe des Einfügebereichs oder sogar die Positionierung des Einfügebereichs an völlig willkürlichen Positionen.

```python
# Wir verwenden die Achsen-Transformation als bbox_transform. Daher muss die Begrenzungsbox
# in Achsenkoordinaten angegeben werden ((0, 0) ist die untere linke Ecke
# der Achse, (1, 1) ist die obere rechte Ecke).
# Die Begrenzungsbox (.2,.4,.6,.5) beginnt bei (.2,.4) und reicht bis (.8,.9)
# in diesen Koordinaten.
# Innerhalb dieser Begrenzungsbox wird ein Einfügebereich mit der Hälfte der Breite der Begrenzungsbox und
# drei Viertel der Höhe der Begrenzungsbox erstellt. Die untere linke Ecke
# des Einfügebereichs wird mit der unteren linken Ecke der Begrenzungsbox ausgerichtet (loc=3).
# Der Einfügebereich wird dann um die standardmäßige 0,5 Einheiten der Schriftgröße versetzt.
axins = inset_axes(ax, width="50%", height="75%",
                   bbox_to_anchor=(.2,.4,.6,.5),
                   bbox_transform=ax.transAxes, loc=3)
```
