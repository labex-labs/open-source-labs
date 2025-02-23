# Button-Füllanimation

`index.html` und `style.css` wurden bereits in der VM zur Verfügung gestellt.

Um eine Füllanimation beim Hovern zu erstellen, können Sie die `Farbe` und `Hintergrund`-Eigenschaften festlegen und einen geeigneten `Übergang` anwenden, um die Änderungen zu animieren. Um die Animation beim Hovern auszulösen, verwenden Sie die `:hover`-Pseudoklasse, um die `Hintergrund`- und `Farbe`-Eigenschaften des Elements zu ändern. Hier ist ein Beispielcodeausschnitt:

```html
<button class="animated-fill-button">Submit</button>
```

```css
.animated-fill-button {
  padding: 20px;
  background: #fff;
  color: #000;
  border: 1px solid #000;
  cursor: pointer;
  transition: 0.3s all ease-in-out;
}

.animated-fill-button:hover {
  background: #000;
  color: #fff;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
