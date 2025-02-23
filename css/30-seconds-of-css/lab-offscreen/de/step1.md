# Außerhalb des sichtbaren Bereichs

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Diese Technik verbirgt ein Element im DOM vollständig, während es weiterhin zugänglich bleibt. Um dies zu erreichen, können Sie die folgenden Schritte ausführen:

- Entfernen Sie alle Kanten und Innenabstände und verstecken Sie das Überlaufen des Elements.
- Verwenden Sie `clip`, um sicherzustellen, dass kein Teil des Elements sichtbar ist.
- Legen Sie die `Höhe` und `Breite` des Elements auf `1px` fest und negieren Sie sie mit `margin: -1px`.
- Verwenden Sie `position: absolute`, um zu verhindern, dass das Element im DOM Platz einnimmt.
- Beachten Sie, dass diese Technik im Hinblick auf Zugänglichkeit und Layout-Freundlichkeit eine bessere Alternative zu `display: none` (nicht lesbar für Bildschirmleser) und `visibility: hidden` (nimmt physischen Platz im DOM ein) ist.

Hier ist ein Beispiel dafür, wie Sie diese Technik in HTML und CSS verwenden können:

```html
<a class="button" href="https://google.com">
  Learn More <span class="offscreen">about pants</span>
</a>
```

```css
.offscreen {
  border: 0;
  clip: rect(0 0 0 0);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
