# Erstellen der Keyframes-Animation

CSS-Animationen funktionieren, indem Keyframes definiert werden, die die Stile angeben, die ein Element zu verschiedenen Zeitpunkten während der Animationssequenz haben soll. Lassen Sie uns die Keyframes für unsere Zoom-In-Zoom-Out-Animation erstellen.

1. Öffnen Sie erneut die Datei `style.css` und fügen Sie am Ende folgenden Code hinzu:

```css
@keyframes zoom-in-zoom-out {
  0% {
    transform: scale(1, 1);
  }
  50% {
    transform: scale(1.5, 1.5);
  }
  100% {
    transform: scale(1, 1);
  }
}
```

2. Lassen Sie uns verstehen, was dieser Code tut:
   - `@keyframes` ist eine CSS-At-Regel, die die Stadien und Stile einer Animation definiert.
   - `zoom-in-zoom-out` ist der Name, den wir unserer Animation geben (wir werden diesen Namen später referenzieren).
   - Innerhalb der Keyframes definieren wir, was zu verschiedenen Zeitpunkten der Animation passiert:
     - Bei `0%` (zum Start) hat das Element seine normale Größe mit `scale(1, 1)`.
     - Bei `50%` (zur Hälfte der Animation) wächst das Element auf das 1,5-fache seiner Größe mit `scale(1.5, 1.5)`.
     - Bei `100%` (zum Ende) kehrt das Element zu seiner normalen Größe zurück.
   - Die `transform`-Eigenschaft mit der `scale()`-Funktion ändert die Größe des Elements.

3. Speichern Sie die Datei `style.css` nach dem Hinzufügen dieser Keyframes.

Die Keyframes definieren, was unsere Animation tun wird, aber wir haben sie noch nicht auf unser Element angewendet. Im nächsten Schritt werden wir die Animation mit unserer Box verbinden.
