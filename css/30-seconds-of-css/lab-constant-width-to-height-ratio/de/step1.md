# Konstantes Verhältnis von Breite zu Höhe

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Dieser Codeausschnitt gewährleistet, dass ein Element mit variabler `width` einen proportionalen `height`-Wert behält. Um dies zu erreichen, wenden Sie `padding-top` auf das `::before`-Pseudo-Element an, sodass die `height` des Elements einem bestimmten Prozentsatz seiner `width` entspricht. Das Verhältnis von `height` zu `width` kann nach Bedarf geändert werden. Beispielsweise wird ein `padding-top` von `100%` ein responsives Quadrat mit einem 1:1-Verhältnis erzeugen. Um diesen Code zu verwenden, fügen Sie einfach folgenden HTML-Code hinzu:

```html
<div class="constant-width-to-height-ratio"></div>
```

Dann fügen Sie folgenden CSS-Code hinzu:

```css
.constant-width-to-height-ratio {
  background: #9c27b0;
  width: 50%;
}

.constant-width-to-height-ratio::before {
  content: "";
  padding-top: 100%;
  float: left;
}

.constant-width-to-height-ratio::after {
  content: "";
  display: block;
  clear: both;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
