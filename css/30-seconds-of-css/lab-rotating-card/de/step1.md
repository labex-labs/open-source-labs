# Rotierende Karte

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine zweiseitige Karte zu erstellen, die beim Hovern rotiert, folgen Sie diesen Schritten:

1. Legen Sie die `backface-visibility` der Karten auf `none` fest, um zu verhindern, dass die Rückseite standardmäßig sichtbar ist.
2. Initial legen Sie `rotateY(-180deg)` für die Rückseite der Karte und `rotateY(0deg)` für die Vorderseite der Karte fest.
3. Beim Hovern legen Sie `rotateY(180deg)` für die Vorderseite der Karte und `rotateY(0deg)` für die Rückseite der Karte fest.
4. Legen Sie einen passenden `Perspektivwert` fest, um den Rotiereffekt zu erzeugen.

Hier ist ein Beispiel für HTML- und CSS-Code:

```html
<div class="card">
  <div class="card-side front">
    <div>Front Seite</div>
  </div>
  <div class="card-side back">
    <div>Rückseite</div>
  </div>
</div>
```

```css
.card {
  perspective: 150rem;
  position: relative;
  height: 40rem;
  max-width: 400px;
  margin: 2rem;
  box-shadow: none;
  background: none;
}

.card-side {
  height: 35rem;
  border-radius: 15px;
  transition: all 0.8s ease;
  backface-visibility: hidden;
  position: absolute;
  top: 0;
  left: 0;
  width: 80%;
  padding: 2rem;
  color: white;
}

.card-side.back {
  transform: rotateY(-180deg);
  background: linear-gradient(43deg, #4158d0 0%, #c850c0 46%, #ffcc70 100%);
}

.card-side.front {
  background: linear-gradient(160deg, #0093e9 0%, #80d0c7 100%);
}

.card:hover.card-side.front {
  transform: rotateY(180deg);
}

.card:hover.card-side.back {
  transform: rotateY(0deg);
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite zu Vorschauen.
