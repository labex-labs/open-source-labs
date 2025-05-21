# Erstellen der HTML-Struktur

Nachdem wir nun die Projekt-Dateien verstanden haben, erstellen wir die HTML-Struktur für unser Schachbrettmuster.

1. Öffnen Sie erneut die Datei `index.html` im Editor.

2. Wir müssen ein Container-Element für unser Schachbrettmuster hinzufügen. Innerhalb des `<body>`-Tags ersetzen Sie den Kommentar durch ein `<div>`-Element mit der Klasse "checkerboard":

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Checkerboard Pattern</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div class="checkerboard"></div>
  </body>
</html>
```

3. Speichern Sie die Datei `index.html`, indem Sie Strg+S drücken oder auf Datei > Speichern klicken.

4. Fügen wir nun einige grundlegende CSS-Regeln hinzu, um die Abmessungen unseres Schachbretts zu definieren. Öffnen Sie die Datei `style.css` und fügen Sie den folgenden Code hinzu:

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
}
```

Dieser CSS-Code macht Folgendes:

- Setzt die Breite und Höhe unseres Schachbretts auf 240 Pixel
- Setzt die Hintergrundfarbe auf Weiß (#fff)

5. Speichern Sie die Datei `style.css`.

6. Aktualisieren Sie den Tab **Web 8080**, um die Änderungen zu sehen.

Sie sollten jetzt ein weißes Quadrat mit einer Breite und Höhe von 240 Pixeln sehen. Dies wird die Leinwand für unser Schachbrettmuster sein.
