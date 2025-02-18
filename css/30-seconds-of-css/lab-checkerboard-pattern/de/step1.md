# Schachbrettmuster als Hintergrund

`index.html` und `style.css` wurden bereits in der virtuellen Maschine (VM) bereitgestellt.

Um ein Schachbrettmuster als Hintergrund zu erstellen, befolgen Sie diese Schritte:

1. Setzen Sie die Eigenschaft `background-color` auf weiß.
2. Verwenden Sie `background-image` mit zwei `linear-gradient()`-Werten, jeweils mit einem anderen Winkel, um das Schachbrettmuster zu erstellen. Beispielsweise setzen Sie einen Winkel auf `45deg` und den anderen auf `-45deg`.
3. Geben Sie die Größe des Musters mit `background-size` an. Beispielsweise wird `60px 60px` ein Muster in der Größe 60 x 60 Pixel erstellen.
4. Verwenden Sie `background-repeat`, um die Wiederholung des Musters festzulegen. Beispielsweise wird `repeat` das Muster in beide Richtungen wiederholen.
5. Beachten Sie, dass die Eigenschaften `height` und `width` des Elements aus Demonstrationsgründen auf 240px festgelegt sind.

Hier ist ein Beispiel für ein HTML-Element mit der Klasse `.checkerboard`:

```html
<div class="checkerboard"></div>
```

Und hier ist der entsprechende CSS-Code:

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image:
    linear-gradient(
      45deg,
      #000 25%,
      transparent 25%,
      transparent 75%,
      #000 75%,
      #000
    ),
    linear-gradient(
      -45deg,
      #000 25%,
      transparent 25%,
      transparent 75%,
      #000 75%,
      #000
    );
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

Klicken Sie bitte auf 'Go Live' in der unteren rechten Ecke, um den Web-Service auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite zu previewen.
