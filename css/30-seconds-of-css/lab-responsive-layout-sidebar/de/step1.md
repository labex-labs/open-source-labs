# Responsives Layout mit Sidebar

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um ein responsives Layout mit einem Inhaltsbereich und einer Sidebar zu erstellen, verwenden Sie `display: grid` auf dem Elterncontainer, `minmax()` für die zweite Spalte (Sidebar), um es zwischen `150px` und `20%` aufnehmen zu lassen, und `1fr` für die erste Spalte (Hauptinhalt), um den Rest des verbleibenden Raums zu belegen. Hier ist ein Beispiel für HTML- und CSS-Code:

```html
<div class="container">
  <main>Dieses Element hat eine Größe von 1fr.</main>
  <aside>Min: 150px / Max: 20%</aside>
</div>
```

```css
.container {
  display: grid;
  grid-template-columns: 1fr minmax(150px, 20%);
  height: 100px;
}

main,
aside {
  padding: 12px;
  text-align: center;
}

main {
  background: #d4f2c4;
}

aside {
  background: #81cfd9;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
