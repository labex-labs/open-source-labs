# Rahmen mit oberem Dreieck

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um einen Inhaltscontainer mit einem Dreieck oben zu erstellen, folgen Sie diesen Schritten:

1. Verwenden Sie die Pseudoelemente `::before` und `::after`, um zwei Dreiecke zu erstellen.
2. Legen Sie die `border-color` und `background-color` der Dreiecke so fest, dass sie mit dem Container übereinstimmen.
3. Legen Sie die `border-width` des `::before`-Dreiecks um `1px` größer als die des `::after`-Dreiecks fest, um als Rahmen zu fungieren.
4. Positionieren Sie das `::after`-Dreieck `1px` rechts vom `::before`-Dreieck, um den linken Rahmen sichtbar zu machen.

Hier ist ein Beispiel für den HTML-Code des Containers:

```html
<div class="container">Border with top triangle</div>
```

Und hier ist der entsprechende CSS-Code:

```css
.container {
  position: relative;
  background: #ffffff;
  padding: 15px;
  border: 1px solid #dddddd;
  margin-top: 20px;
}

.container::before,
.container::after {
  content: "";
  position: absolute;
  bottom: 100%;
  left: 19px;
  border: 11px solid transparent;
}

.container::before {
  border-bottom-color: #dddddd;
}

.container::after {
  left: 20px;
  border: 10px solid transparent;
  border-bottom-color: #ffffff;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
