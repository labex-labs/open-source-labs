# Liste mit fließenden Abschnittstiteln

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine Liste mit fließenden Überschriften für jeden Abschnitt zu erstellen, folgen Sie diesen Schritten:

1. Wenden Sie `overflow-y: auto` auf den Listencontainer an, um vertikalen Überlauf zu ermöglichen.
2. Verwenden Sie `display: grid` auf dem inneren Container (`<dl>`), um ein Layout mit zwei Spalten zu erstellen.
3. Legen Sie Überschriften (`<dt>`) auf `grid-column: 1` und Inhalte (`<dd>`) auf `grid-column: 2` fest.
4. Legen Sie schließlich `position: sticky` und `top: 0,5rem` auf Überschriften an, um einen fließenden Effekt zu erzeugen.

Hier ist der HTML-Code:

```html
<div class="container">
  <div class="floating-stack">
    <dl>
      <dt>A</dt>
      <dd>Algerien</dd>
      <dd>Angola</dd>

      <dt>B</dt>
      <dd>Benin</dd>
      <dd>Botswana</dd>
      <dd>Burkina Faso</dd>
      <dd>Burundi</dd>

      <dt>C</dt>
      <dd>Kap Verde</dd>
      <dd>Kamerun</dd>
      <dd>Zentralafrikanische Republik</dd>
      <dd>Tschad</dd>
      <dd>Komoren</dd>
      <dd>Kongo, Demokratische Republik des</dd>
      <dd>Kongo, Republik des</dd>
      <dd>Ivory Coast (Côte d'Ivoire)</dd>

      <dt>D</dt>
      <dd>Dschibuti</dd>

      <dt>E</dt>
      <dd>Ägypten</dd>
      <dd>Äquatorialguinea</dd>
      <dd>Eritrea</dd>
      <dd>Eswatini (früher Swasiland)</dd>
      <dd>Äthiopien</dd>
    </dl>
  </div>
</div>
```

Und hier ist der CSS-Code:

```css
.container {
  display: grid;
  place-items: center;
  min-height: 400px;
}

.floating-stack {
  background: #455a64;
  color: #fff;
  height: 80vh;
  width: 320px;
  border-radius: 1rem;
  overflow-y: auto;
}

.floating-stack > dl {
  margin: 0 0 1rem;
  display: grid;
  grid-template-columns:
    2,
    5rem 1fr;
  align-items: center;
}

.floating-stack dt {
  position: sticky;
  top: 0, 5rem;
  left: 0, 5rem;
  font-weight: bold;
  background: #263238;
  color: #cfd8dc;
  height: 2rem;
  width: 2rem;
  border-radius: 50%;
  padding:
    0,
    25rem 1rem;
  grid-column: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
}

.floating-stack dd {
  grid-column: 2;
  margin: 0;
  padding: 0, 75rem;
}

.floating-stack > dl:first-of-type > dd:first-of-type {
  margin-top: 0, 25rem;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
