# Auswahl deaktivieren

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um den Inhalt eines Elements nicht auswählbar zu machen, fügen Sie der Selektor die CSS-Eigenschaft `user-select: none` hinzu. Diese Methode ist jedoch nicht vollständig sicher, um zu verhindern, dass Benutzer Inhalte kopieren.

Beispiel:

```html
<p>You can select me.</p>
<p class="unselectable">You can't select me!</p>
```

```css
.unselectable {
  user-select: none;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
