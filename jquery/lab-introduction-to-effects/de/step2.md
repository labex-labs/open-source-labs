# Anzeige basierend auf dem aktuellen Sichtbarkeitsstatus ändern

Mit jQuery können Sie auch die Sichtbarkeit eines Inhalts basierend auf seinem aktuellen Sichtbarkeitsstatus ändern. `.toggle()` zeigt Inhalte an, die derzeit ausgeblendet sind, und blendet Inhalte aus, die derzeit sichtbar sind. Sie können die gleichen Argumente an `.toggle()` übergeben wie an jede der oben genannten Effektmethoden.

```js
// Wechselt die Anzeige aller Absätze sofort
$("p").toggle();

// Wechselt die Anzeige aller Divs innerhalb von 1,8 Sekunden
$("div").toggle(1800);
```

`.toggle()` verwendet eine Kombination aus Slide- und Fade-Effekten, genauso wie `.show()` und `.hide()`.

> Sie können die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
