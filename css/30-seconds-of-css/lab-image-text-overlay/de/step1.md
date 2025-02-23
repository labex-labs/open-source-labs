# Bild mit Textüberschrift

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um ein Bild mit einer Textüberschrift anzuzeigen, verwenden Sie die `<figure>`- und `<figcaption>`-Elemente. Verwenden Sie die `linear-gradient`-Eigenschaft in CSS, um die Überlagerungseffekt über dem Bild zu erstellen. Hier ist ein Beispielcodeausschnitt:

```html
<figure class="text-overlay-image">
  <img src="https://picsum.photos/id/971/400/400.jpg" />
  <figcaption>
    <h3>Business <br />Pricing</h3>
  </figcaption>
</figure>
```

```css
.text-overlay-image {
  box-sizing: border-box;
  position: relative;
  margin: 8px;
  max-width: 400px;
  max-height: 400px;
  width: 100%;
}

.text-overlay-image figcaption {
  box-sizing: border-box;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  background: linear-gradient(0deg, #00000088 30%, #ffffff44 100%);
  color: #fff;
  padding: 16px;
  font: 700 28px/1.2 sans-serif;
}

.text-overlay-image figcaption h3 {
  margin: 0;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite im Vorschau zu sehen.
