# Erstellen eines Textfelds

```python
plt.text(0.6, 0.7, "eggs", size=50, rotation=30.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
```

Wir erstellen ein Textfeld, das das Wort "Eier" enthält, indem wir die `text()`-Methode verwenden. Der `bbox`-Parameter wird verwendet, um das Textfeld zu stylen. Der `boxstyle`-Parameter ist auf "round" gesetzt, um ein abgerundetes Textfeld zu erstellen, während die `ec`- und `fc`-Parameter die Kanten- und Flächenefarben des Textfelds festlegen. Der `size`-Parameter setzt die Schriftgröße, der `rotation`-Parameter setzt den Rotationswinkel und die `ha`- und `va`-Parameter setzen die horizontale und vertikale Ausrichtung des Textes im Textfeld.
