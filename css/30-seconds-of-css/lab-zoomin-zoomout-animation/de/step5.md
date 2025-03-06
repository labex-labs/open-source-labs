# Experimentieren mit Animations-Eigenschaften

Lassen Sie uns unsere Animation anpassen, indem wir mit verschiedenen Animations-Eigenschaften experimentieren. Dies wird Ihnen helfen, zu verstehen, wie diese Eigenschaften das Animationsverhalten beeinflussen.

1. Öffnen Sie die Datei `style.css` und ändern Sie den Selektor `.zoom-in-out-box`, um verschiedene Animations-Eigenschaften auszuprobieren:

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 2s ease-in-out infinite;
  /* Add a slight rotation during the animation */
  border-radius: 10px;
}
```

2. Lassen Sie uns verstehen, was wir geändert haben:

   - Wir haben die Animationsdauer auf `2s` (2 Sekunden) verlängert.
   - Wir haben die Timing-Funktion auf `ease-in-out` geändert, was sowohl den Anfang als auch das Ende der Animation glatt macht.
   - Wir haben einen `border-radius` von 10px hinzugefügt, um die Ecken unserer Box abzurunden.

3. Lassen Sie uns auch unsere Keyframes ändern, um einen Rotationseffekt hinzuzufügen:

```css
@keyframes zoom-in-zoom-out {
  0% {
    transform: scale(1, 1) rotate(0deg);
  }
  50% {
    transform: scale(1.5, 1.5) rotate(45deg);
    background-color: #2196f3;
  }
  100% {
    transform: scale(1, 1) rotate(0deg);
  }
}
```

4. In dieser aktualisierten Keyframes-Definition:

   - Wir haben die `rotate()`-Funktion zur `transform`-Eigenschaft hinzugefügt.
   - Bei 50% der Animation rotiert das Element jetzt um 45 Grad, während es sich vergrößert.
   - Wir ändern auch die Hintergrundfarbe auf blau bei 50% der Animation.

5. Speichern Sie die Datei `style.css` nach diesen Änderungen.

6. Aktualisieren Sie die Registerkarte **Web 8080**, um Ihre verbesserte Animation zu sehen.

Ihre Animation sollte jetzt langsamer sein (2 Sekunden pro Zyklus), abgerundete Ecken haben, sich beim Zoomen drehen und die Farbe halbwegs durch die Animation ändern. Dies zeigt, wie CSS-Animationen mehrere Eigenschaftsänderungen kombinieren können, um reiche visuelle Effekte zu erzielen.

Fühlen Sie sich frei, weiter mit verschiedenen Eigenschaften und Werten zu experimentieren, um zu sehen, wie sie Ihre Animation beeinflussen.
