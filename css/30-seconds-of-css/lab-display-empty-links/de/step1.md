# Links ohne Text formatieren

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um die Link-URL für Links ohne Text anzuzeigen, können Sie die Pseudoklasse `:empty` verwenden, um solche Links auszuwählen, die Pseudoklasse `:not` verwenden, um Links mit Text auszuschließen, und die Eigenschaft `content` in Kombination mit der Funktion `attr()`, um die Link-URL im Pseudoelement `::before` anzuzeigen. Hier ist ein Beispielcodeausschnitt:

```html
<a href="https://30secondsofcode.org"></a>
```

```css
a[href^="http"]:empty::before {
  content: attr(href);
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
