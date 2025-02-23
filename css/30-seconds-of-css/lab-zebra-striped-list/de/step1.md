# Streifenförmige Liste

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine Liste mit abwechselnden Hintergrundfarben zu erstellen, verwenden Sie die pseudo-klassenselektoren `:nth-child(odd)` oder `:nth-child(even)`, um eine unterschiedliche `background-color` auf Elemente basierend auf ihrer Position unter den Geschwistern anzuwenden. Dies kann auf verschiedene HTML-Elemente wie `<div>`, `<tr>`, `<p>`, `<ol>` usw. angewendet werden.

Hier ist ein Beispiel dafür, wie man eine streifenförmige Liste mit `<li>`-Elementen erstellt:

```html
<ul>
  <li>Element 01</li>
  <li>Element 02</li>
  <li>Element 03</li>
  <li>Element 04</li>
  <li>Element 05</li>
</ul>
```

```css
li:nth-child(odd) {
  background-color: #999;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
