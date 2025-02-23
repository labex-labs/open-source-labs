# Buttonschrumpfanimation

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine Schrumpfanimation beim Hovern für ein Element zu erstellen, können Sie eine geeignete `transition`-Eigenschaft verwenden, um Änderungen zu animieren, und die `:hover`-Pseudoklasse, um die Animation auszulösen. Beispielsweise, wenn Sie einen Button mit der Klasse `button-shrink` verkleinern möchten, wenn ein Benutzer darüber fährt, können Sie die folgende CSS hinzufügen:

```css
.button-shrink {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.button-shrink:hover {
  transform: scale(0.8);
}
```

Dies wird einen Übergangseffekt auf alle Eigenschaften des Buttons anwenden, wenn sich etwas ändert, und wenn der Benutzer darüber fährt, wird der Button auf 80% seiner ursprünglichen Größe verkleinert. Der HTML-Code für den Button lautet wie folgt:

```html
<button class="button-shrink">Submit</button>
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
