# Shape Separator

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um ein Separatorelement zwischen zwei verschiedenen Blöcken mit einer SVG-Shape zu erstellen, folgen Sie diesen Schritten:

1. Verwenden Sie das `::after`-Pseudo-Element.
2. Fügen Sie die SVG-Shape (ein 24x12-Dreieck) über eine Data URI mithilfe der `background-image`-Eigenschaft hinzu. Das Hintergrundbild wird standardmäßig wiederholt und die gesamte Fläche des Pseudo-Elements abdecken.
3. Legen Sie die gewünschte Farbe für den Separator mithilfe der `background`-Eigenschaft des übergeordneten Elements fest.

Verwenden Sie folgenden HTML-Code:

```html
<div class="shape-separator"></div>
```

Und wenden Sie folgende CSS-Regeln an:

```css
.shape-separator {
  position: relative;
  height: 48px;
  background: #9c27b0;
}

.shape-separator::after {
  content: "";
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 12'%3E%3Cpath d='m12 0l12 12h-24z' fill='transparent'/%3E%3C/svg%3E");
  position: absolute;
  width: 100%;
  height: 12px;
  bottom: 0;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
