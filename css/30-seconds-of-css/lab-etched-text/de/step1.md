# Geätzter Text

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um einen "geätzten" oder gravierten Effekt für Text auf einem Hintergrund zu erstellen, verwenden Sie die folgenden CSS-Eigenschaften:

```css
.etched-text {
  text-shadow: 0 2px white;
  font-size: 1.5rem;
  font-weight: bold;
  color: #b8bec5;
}
```

Die `text-shadow`-Eigenschaft erzeugt einen weißen Schatten, der horizontal um `0px` und vertikal um `2px` von der Ausgangsposition versetzt ist. Stellen Sie sicher, dass der Hintergrund dunkler als der Schatten ist, damit der Effekt funktioniert. Darüber hinaus sollte die Textfarbe etwas verblasst sein, um es so aussehen zu lassen, als wäre er aus dem Hintergrund geschnitzt. Schließlich wenden Sie die `etched-text`-Klasse auf das gewünschte HTML-Element, wie z. B. einen Absatz, an, um den Effekt zu erzielen.

```html
<p class="etched-text">I appear etched into the background.</p>
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
