# System-Schriftstapel

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um ein Gefühl für native Anwendungen zu erzeugen, verwenden Sie die native Schrift des Betriebssystems. Definieren Sie eine Liste von Schriften mit `font-family`. Der Browser sucht nach jeder aufeinanderfolgenden Schrift und wählt, wenn möglich, die erste aus. Wenn er die Schrift nicht finden kann (auf dem System oder in der CSS definiert), greift er auf die nächste zurück. Verwenden Sie `-apple-system` für San Francisco auf iOS und macOS (nicht Chrome) und `BlinkMacSystemFont` für San Francisco auf macOS Chrome. Für Windows 10 verwenden Sie `'Segoe UI'`, für Android verwenden Sie `Roboto`, für Linux mit KDE verwenden Sie `Oxygen-Sans`, für Ubuntu (alle Varianten) verwenden Sie `Ubuntu` und für Linux mit GNOME Shell verwenden Sie `Cantarell`. Für macOS 10.10 und älter verwenden Sie `'Helvetica Neue'` und `Helvetica`. Für eine Rückfall-Schriftart ohne Serifen, die von allen Betriebssystemen weitgehend unterstützt wird, verwenden Sie `Arial`. Um die Systemschrift auf einen bestimmten Text anzuwenden, verwenden Sie den folgenden HTML- und CSS-Code:

```html
<p class="system-font-stack">This text uses the system font.</p>
```

```css
.system-font-stack {
  font-family:
    -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu,
    Cantarell, "Helvetica Neue", Helvetica, Arial, sans-serif;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
