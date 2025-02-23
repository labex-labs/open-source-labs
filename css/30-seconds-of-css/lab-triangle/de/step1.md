# Dreieck

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine dreieckige Form mit reinem CSS zu erstellen, folgen Sie diesen Schritten:

1. Verwenden Sie drei Bordüren mit der gleichen `border-width` (`20px`), um die dreieckige Form zu erstellen.
2. Setzen Sie die `border-color` der gegenüberliegenden Seite, wohin das Dreieck zeigt, auf die gewünschte Farbe. Die angrenzenden Bordüren sollten eine `border-color` von `transparent` haben.
3. Um die Größe des Dreiecks anzupassen, ändern Sie die `border-width`-Werte.

Hier ist ein Beispielcodeausschnitt:

```html
<div class="triangle"></div>
```

```css
.triangle {
  width: 0;
  height: 0;
  border-top: 20px solid #9c27b0;
  border-left: 20px solid transparent;
  border-right: 20px solid transparent;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
