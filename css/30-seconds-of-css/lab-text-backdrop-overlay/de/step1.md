# Überlagerung von Text auf Bildern

`index.html` und `style.css` wurden bereits in der VM zur Verfügung gestellt.

Um Text auf einem Bild mit einer Überlagerung anzuzeigen, verwenden Sie die Eigenschaft `backdrop-filter`, um einen Effekt von `blur(14px)` und `brightness(80%)` anzuwenden. Dadurch wird sichergestellt, dass der Text unabhängig von dem Hintergrundbild und der Hintergrundfarbe lesbar ist. Hier ist ein Beispiel für HTML-Code:

```html
<div>
  <h3 class="text-overlay">Hello, World</h3>
  <img src="https://picsum.photos/id/1050/1200/800" />
</div>
```

Und der entsprechende CSS-Code:

```css
div {
  position: relative;
}

.text-overlay {
  position: absolute;
  top: 0;
  left: 0;
  padding: 1rem;
  font-size: 2rem;
  font-weight: 300;
  color: white;
  backdrop-filter: blur(14px) brightness(80%);
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
