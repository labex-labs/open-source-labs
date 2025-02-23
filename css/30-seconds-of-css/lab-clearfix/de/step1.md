# Clearfix

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um sicherzustellen, dass ein Element seine Kinder automatisch aufräumt, wenn `float` verwendet wird, um Layouts zu erstellen, können Sie das pseudo-Element `::after` verwenden und `content: ''` anwenden, um es auf das Layout wirken zu lassen. Darüber hinaus verwenden Sie `clear: both`, um das Element von links und rechts gefloatenen Elementen zu befreien. Diese Technik funktioniert jedoch nur dann richtig, wenn im Container keine nicht gefloatenen Kinder vorhanden sind und keine hohen Floats vor dem clearfixed-Container, aber im gleichen Formatierungskontext (z.B. gefloate Spalten) vorhanden sind. Beispielsweise:

```html
<div class="clearfix">
  <div class="floated">float a</div>
  <div class="floated">float b</div>
  <div class="floated">float c</div>
</div>
```

```css
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}

.floated {
  float: left;
  padding: 4px;
}
```

Beachten Sie, dass es empfohlen wird, einen moderneren Ansatz wie die Flexbox- oder Grid-Layouts zu verwenden, anstatt `float` zum Erstellen von Layouts zu verwenden.

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
