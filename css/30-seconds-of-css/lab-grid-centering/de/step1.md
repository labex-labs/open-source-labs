# Grid-Zentrierung

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um ein Kind-Element sowohl horizontal als auch vertikal in einem Eltern-Element zu zentrieren, folgen Sie diesen Schritten:

1. Erstellen Sie ein Grid-Layout mit `display: grid`.
2. Verwenden Sie `justify-content: center`, um das Kind horizontal zu zentrieren.
3. Verwenden Sie `align-items: center`, um das Kind vertikal zu zentrieren.

Hier ist ein Beispiel für eine HTML-Struktur:

```html
<div class="parent">
  <div class="child">Zentrierter Inhalt.</div>
</div>
```

Und die entsprechende CSS:

```css
.parent {
  display: grid;
  justify-content: center;
  align-items: center;
  height: 100px;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
