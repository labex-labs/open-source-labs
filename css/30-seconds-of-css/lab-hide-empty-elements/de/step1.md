# Leere Elemente verstecken

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um Elemente ohne Inhalt zu verstecken, verwenden Sie die `:empty`-Pseudo-Klasse. Beispielsweise, wenn Sie folgenden HTML-Code haben:

```html
<p>Lorem ipsum dolor sit amet. <button></button></p>
```

Sie können folgenden CSS-Code verwenden, um das Element `button` ohne Inhalt zu verstecken:

```css
p:empty {
  display: none;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
