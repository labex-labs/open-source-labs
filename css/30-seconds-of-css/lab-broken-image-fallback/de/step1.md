# Alternative für Bilder, die nicht geladen werden können

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Wenn ein Bild nicht geladen werden kann, wird der Benutzer eine Fehlermeldung angezeigt. Um dies zu tun, wenden Sie Stile auf das `img`-Element an, als wäre es ein Textcontainer, und legen Sie seine Anzeige auf block und seine Breite auf 100% fest. Verwenden Sie die pseudo-Elemente `::before` und `::after`, um die Fehlermeldung und die Bild-URL jeweils anzuzeigen. Diese Elemente werden nur angezeigt, wenn das Bild nicht geladen werden kann.

Hier ist ein Beispielcodeausschnitt:

```html
<img src="https://nowhere.to.be/found.jpg" />
```

```css
img {
  display: block;
  width: 100%;
  height: auto;
  line-height: 2;
  position: relative;
  text-align: center;
  font-family: sans-serif;
  font-weight: 300;
}

img::before {
  content: "Sorry, this image is unavailable.";
  display: block;
  margin-bottom: 8px;
}

img::after {
  content: "(url: " attr(src) ")";
  display: block;
  font-size: 12px;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
