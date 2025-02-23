# Liste mit klebenden Abschnittstiteln

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine Liste mit klebenden Überschriften für jeden Abschnitt zu erstellen, folgen Sie diesen Schritten:

1. Erlauben Sie es der Listenumgebung (`<dl>`), vertikal zu überlaufen, indem Sie `overflow-y: auto` verwenden.
2. Befestigen Sie die Überschriften (`<dt>`) oben am Container, indem Sie ihre `position` auf `sticky` setzen und `top: 0` anwenden.
3. Verwenden Sie den folgenden HTML- und CSS-Code:

HTML:

```html
<div class="container">
  <dl class="sticky-stack">
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
    <dd>Ivory Coast (Cote d'Ivoire)</dd>

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
```

CSS:

```css
.container {
  display: grid;
  place-items: center;
  min-height: 400px;
}

.sticky-stack {
  background: #37474f;
  color: #fff;
  margin: 0;
  height: 320px;
  border-radius: 1rem;
  overflow-y: auto;
}

.sticky-stack dt {
  position: sticky;
  top: 0;
  font-weight: bold;
  background: #263238;
  color: #cfd8dc;
  padding: 0.25rem 1rem;
}

.sticky-stack dd {
  margin: 0;
  padding: 0.75rem 1rem;
}

.sticky-stack dd + dt {
  margin-top: 1rem;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
