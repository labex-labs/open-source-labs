# 3-Kachel-Layout

In der VM wurden bereits `index.html` und `style.css` bereitgestellt.

Um ein 3-Kachel-Layout zu erstellen, verwenden Sie `display: inline-block` anstelle von `float`, `flex` oder `grid`. Verwenden Sie `width` in Kombination mit `calc`, um die Breite des Containers gleichmäßig in 3 Spalten zu teilen. Um Leerraum zu vermeiden, legen Sie `font-size` für `.tiles` auf `0` und für `<h2>`-Elemente auf `20px` fest, um den Text anzuzeigen. Beachten Sie, dass das Verwenden von `font-size: 0` zur Bekämpfung von Leerraum zwischen Blöcken möglicherweise Nebenwirkungen verursachen kann, wenn Sie relative Maße (z.B. `em`) verwenden.

```html
<div class="tiles">
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
</div>
```

```css
.tiles {
  width: 600px;
  font-size: 0;
  margin: 0 auto;
}

.tile {
  width: calc(600px / 3);
  display: inline-block;
}

.tile h2 {
  font-size: 20px;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
