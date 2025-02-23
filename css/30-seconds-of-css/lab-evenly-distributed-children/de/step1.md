# Gleichmäßig Verteilte Kinder

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um die Kinderelemente innerhalb eines Elterntelements gleichmäßig zu verteilen, verwenden Sie das Flexbox-Layout, indem Sie die `display`-Eigenschaft des Elterntelements auf `flex` setzen. Um die Kinder horizontal mit gleichen Abständen zu verteilen, verwenden Sie `justify-content: space-between`. Um die Kinder mit Abstand dazwischen zu verteilen, verwenden Sie `justify-content: space-around`. Hier ist ein Beispiel:

```html
<div class="evenly-distributed-children">
  <p>Item1</p>
  <p>Item2</p>
  <p>Item3</p>
</div>
```

```css
.evenly-distributed-children {
  display: flex;
  justify-content: space-between;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
