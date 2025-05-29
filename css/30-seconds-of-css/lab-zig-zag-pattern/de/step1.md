# Zickzack-Hintergrundmuster

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um ein Zickzack-Hintergrundmuster zu erstellen, folgen Sie diesen Schritten:

1. Legen Sie einen weißen Hintergrund mit `background-color` fest.
2. Erstellen Sie die Teile eines Zickzack-Musters mit `background-image` und vier `linear-gradient()`-Werten.
3. Geben Sie die Größe des Musters mit `background-size` an.
4. Stellen Sie die Teile des Musters an den richtigen Orten mit `background-position` ein.
5. Um das Muster zu wiederholen, verwenden Sie `background-repeat`.
6. **Hinweis:** Die `height` und `width` des Elements sind nur zu Demonstrationszwecken festgelegt.

Hier ist ein Beispielcodeausschnitt:

```html
<div class="zig-zag"></div>
```

```css
.zig-zag {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image:
    linear-gradient(135deg, #000 25%, transparent 25%),
    linear-gradient(225deg, #000 25%, transparent 25%),
    linear-gradient(315deg, #000 25%, transparent 25%),
    linear-gradient(45deg, #000 25%, transparent 25%);
  background-position:
    -30px 0,
    -30px 0,
    0 0,
    0 0;
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
