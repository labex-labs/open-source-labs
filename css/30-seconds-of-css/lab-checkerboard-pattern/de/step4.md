# Vervollständigung des Schachbrettmusters

Jetzt fügen wir den zweiten linearen Farbverlauf hinzu, um unser Schachbrettmuster abzurunden und es über das gesamte Element wiederholbar zu machen.

1. Öffnen Sie erneut die Datei `style.css`.

2. Modifizieren Sie die `.checkerboard`-Klasse, um einen zweiten linearen Farbverlauf hinzuzufügen, der das abwechselnde Muster erzeugt:

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(
      45deg,
      #000 25%,
      transparent 25%,
      transparent 75%,
      #000 75%,
      #000
    ), linear-gradient(-45deg, #000 25%, transparent 25%, transparent 75%, #000
        75%, #000);
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

Was wir hinzugefügt haben:

- Einen zweiten `linear-gradient()`, der dem ersten ähnelt, aber mit einem Winkel von `-45deg`, um das abwechselnde Muster zu erzeugen
- Die Eigenschaft `background-repeat: repeat` sorgt dafür, dass die Muster über das gesamte Element wiederholt werden

Die Kombination dieser beiden Farbverläufe in verschiedenen Winkeln erzeugt das klassische Schachbrettmuster. Der erste Farbverlauf erzeugt eine Reihe von diagonalen Quadraten, während der zweite Farbverlauf eine andere Reihe erzeugt, die die Lücken füllt.

3. Speichern Sie die Datei `style.css`.

4. Aktualisieren Sie den Tab **Web 8080**, um das endgültige Ergebnis zu sehen.

Sie sollten jetzt ein vollständiges Schachbrettmuster mit abwechselnden schwarzen und weißen Quadraten sehen. Das Muster sollte über das gesamte 240x240 Pixel große Element wiederholt werden.

## Funktionsweise des Musters

Der Schachbretteffekt wird erzeugt, indem:

1. Zwei lineare Farbverläufe mit entgegengesetzten Winkeln (45deg und -45deg) verwendet werden
2. Jeder Farbverlauf ein Muster von schwarzen Quadraten in den Ecken erzeugt
3. Die transparenten Bereiche ermöglichen es, dass der weiße Hintergrund durchscheint
4. Die Eigenschaft `background-size` steuert die Größe jedes Quadrats im Muster
5. Die Eigenschaft `background-repeat` lässt das Muster über das gesamte Element wiederholen

Diese Technik zeigt die Stärke von CSS-Farbverläufen bei der Erstellung komplexer Muster ohne die Notwendigkeit von Bilddateien, was zu schnelleren Ladezeiten und besserer Skalierbarkeit führt.
