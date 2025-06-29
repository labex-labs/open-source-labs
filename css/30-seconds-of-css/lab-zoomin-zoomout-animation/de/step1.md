# Verständnis der HTML-Struktur

Bevor wir mit der Erstellung unserer Animation beginnen, müssen wir die HTML-Struktur verstehen, mit der wir arbeiten werden. In diesem Schritt werden wir die bereitgestellte HTML-Datei untersuchen und alle erforderlichen Änderungen vornehmen.

1. Öffnen Sie die Datei `index.html` im Editor.

2. Wenn die Datei leer ist oder fehlt, erstellen Sie sie mit folgendem Inhalt:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Zoom In Zoom Out Animation</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>CSS Animation Demo</h1>
    <p>This box demonstrates a zoom in zoom out animation:</p>

    <div class="zoom-in-out-box"></div>
  </body>
</html>
```

3. Lassen Sie uns verstehen, was diese HTML-Datei macht:
   - Wir haben eine Standard-HTML-Dokumentstruktur mit einem Titel und Viewport-Einstellungen.
   - Wir verlinken auf eine externe CSS-Datei namens `style.css`.
   - Wir fügen eine Überschrift und einen Absatz hinzu, um unsere Demo zu erklären.
   - Am wichtigsten ist, dass wir ein `<div>`-Element mit der Klasse `zoom-in-out-box` haben, das animiert werden wird.

4. Speichern Sie die Datei `index.html`, wenn Sie Änderungen vorgenommen haben.

Dieses div-Element wird unser "Leinwand" für die Erstellung der Animation sein. Im nächsten Schritt werden wir dieses Element mit CSS gestalten.
