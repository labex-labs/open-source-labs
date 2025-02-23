# Dynamischer Schatten

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um einen Schatten zu erstellen, der auf den Farben eines Elements basiert, folge diesen Schritten:

1. Verwende das `::after`-Pseudo-Element mit `position: absolute` und `width` und `height` auf `100%` gesetzt, um den verfügbaren Platz im Eltern-Element zu füllen.

2. Vererbe den `background` des Eltern-Elements, indem du `background: inherit` verwendest.

3. Verschiebe das Pseudo-Element leicht mit `top`. Dann verwende `filter: blur()` um einen Schatten zu erstellen und setze `opacity`, um ihn halbtransparent zu machen.

4. Stelle das Pseudo-Element hinter seinem Eltern-Element, indem du `z-index: -1` setzt. Setze `z-index: 1` auf das Eltern-Element.

Hier ist ein Beispiel für HTML- und CSS-Code:

```html
<div class="dynamic-shadow"></div>
```

```css
.dynamic-shadow {
  position: relative;
  width: 10rem;
  height: 10rem;
  background: linear-gradient(75deg, #6d78ff, #00ffb8);
  z-index: 1;
}

.dynamic-shadow::after {
  content: "";
  width: 100%;
  height: 100%;
  position: absolute;
  background: inherit;
  top: 0.5rem;
  filter: blur(0.4rem);
  opacity: 0.7;
  z-index: -1;
}
```

Bitte klicke in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Dann kannst du die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
