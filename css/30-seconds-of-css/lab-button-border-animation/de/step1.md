# Button-Rahmenanimation

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine Rahmenanimation beim Hovern zu erstellen, können Sie die Pseudoelemente `::before` und `::after` verwenden, um zwei Boxen zu generieren, die 24 Pixel breit sind und über und unter der Box positioniert sind. Anschließend wenden Sie die Pseudoklasse `:hover` an, um die Breite dieser Elemente beim Hovern auf `100%` zu erhöhen und die Übergangsanimation mit `transition` zu animieren.

Hier ist ein Beispielcodeausschnitt:

```html
<button class="animated-border-button">Submit</button>
```

```css
.animated-border-button {
  background-color: #263059;
  border: none;
  color: #ffffff;
  outline: none;
  padding: 12px 40px 10px;
  position: relative;
}

.animated-border-button::before,
.animated-border-button::after {
  border: 0 solid transparent;
  transition: all 0.3s;
  content: "";
  height: 0;
  position: absolute;
  width: 24px;
}

.animated-border-button::before {
  border-top: 2px solid #263059;
  right: 0;
  top: -4px;
}

.animated-border-button::after {
  border-bottom: 2px solid #263059;
  bottom: -4px;
  left: 0;
}

.animated-border-button:hover::before,
.animated-border-button:hover::after {
  width: 100%;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
