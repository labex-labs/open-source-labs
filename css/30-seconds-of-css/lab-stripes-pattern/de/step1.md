# Streifen-Hintergrundmuster

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Dieser Code erstellt ein vertikales Streifenmuster auf einem weißen Hintergrund.

Um das Muster zu erstellen:

- Setzen Sie die Eigenschaft `background-color` auf weiß.
- Verwenden Sie `background-image` mit einem Wert von `linear-gradient()`, um ein vertikales Streifenmuster zu erstellen.
- Setzen Sie die Eigenschaft `background-size`, um die Größe jedes Streifens anzugeben.
- Setzen Sie `background-repeat` auf `repeat`, um das Muster das Element zu füllen.

Beachten Sie, dass die feste `width` und `height` des Elements nur zu Demonstrationszwecken sind.

Hier ist ein Beispiel-Codeausschnitt:

```html
<div class="stripes"></div>
```

```css
.stripes {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(90deg, transparent 50%, #000 50%);
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
