# Erstellen des ersten Farbverlaufs

Jetzt beginnen wir mit der Erstellung unseres Schachbrettmusters mithilfe von CSS-Farbverläufen. Fügen wir zunächst den ersten linearen Farbverlauf hinzu, um einen Teil des Musters zu erstellen.

## Grundlagen zu linearen CSS-Farbverläufen

Mit linearen CSS-Farbverläufen können Sie sanfte Übergänge zwischen zwei oder mehr Farben in einer geraden Linie erstellen. Die Funktion `linear-gradient()` nimmt einen Winkel und eine Reihe von Farbpunkten (color stops) als Parameter. Wir werden diese Technik nutzen, um die Felder unseres Schachbretts zu gestalten.

Folgen Sie diesen Schritten:

1. Öffnen Sie die Datei `style.css`.

2. Modifizieren wir die `.checkerboard`-Klasse, um den ersten linearen Farbverlauf hinzuzufügen:

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
  );
  background-size: 60px 60px;
}
```

Lassen Sie mich erklären, was dieser Farbverlauf bewirkt:

- `45deg` gibt den Winkel des Farbverlaufs an.
- `#000 25%` erzeugt eine schwarze Farbe von 0% bis 25% des verfügbaren Raums.
- `transparent 25%` erzeugt eine transparente Farbe, die ab 25% beginnt.
- `transparent 75%` behält die transparente Farbe bis 75% bei.
- `#000 75%` wechselt ab 75% wieder zur schwarzen Farbe und setzt diese bis zum Ende fort.
- `background-size: 60px 60px` legt die Größe jeder wiederholten Farbverlaufszelle fest.

3. Speichern Sie die Datei `style.css`.

4. Aktualisieren Sie den Tab **Web 8080**, um die Änderungen zu sehen.

Sie sollten jetzt ein Muster erkennen, das sich langsam bildet, aber es ist noch kein vollständiges Schachbrett. Der erste Farbverlauf erzeugt nur einen Teil des Musters. Im nächsten Schritt fügen wir einen zweiten Farbverlauf hinzu, um das Schachbrett zu vervollständigen.
