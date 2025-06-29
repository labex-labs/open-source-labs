# Grundlegende CSS-Stilgestaltung

Nachdem wir nun unsere HTML-Struktur festgelegt haben, erstellen wir die grundlegende CSS-Stilgestaltung für unser Animations-Element.

1. Öffnen Sie die Datei `style.css` im Editor.

2. Wenn die Datei leer ist oder fehlt, erstellen Sie sie mit folgendem Inhalt:

```css
body {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  color: #333;
}

.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
}
```

3. Lassen Sie uns verstehen, was diese CSS-Regeln tun:
   - Wir setzen einige grundlegende Stile für die Seite (Schriftart, Breite und Abstände).
   - Wir gestalten die Überschrift mit einer dunklen Graufarbe.
   - Für unser Animations-Element `.zoom-in-out-box` tun wir Folgendes:
     - Fügen wir einen Abstand von 24px um das Element herum hinzu.
     - Setzen wir seine Breite und Höhe auf 50px.
     - Geben wir ihm eine lebhafte rosa Hintergrundfarbe.

4. Speichern Sie die Datei `style.css` nach diesen Änderungen.

5. Um Ihren Fortschritt zu sehen, klicken Sie auf die Schaltfläche "Go Live" in der unteren rechten Ecke von VSCode. Dadurch wird ein Webserver auf Port 8080 gestartet. Aktualisieren Sie dann die Registerkarte **Web 8080**, um Ihre gestaltete Box zu sehen.

Sie sollten jetzt ein kleines rosa Quadrat auf Ihrer Webseite sehen. Dieses Quadrat ist das Element, das wir in den nächsten Schritten animieren werden.
