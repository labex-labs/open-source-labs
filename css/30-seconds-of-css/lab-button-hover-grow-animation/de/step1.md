# Button-Vergrößerungsanimation

`index.html` und `style.css` wurden bereits in der virtuellen Maschine (VM) bereitgestellt.

Um eine Vergrößerungsanimation beim Überfahren zu erstellen, können Sie eine geeignete `transition` verwenden, um Änderungen am Element zu animieren. Verwenden Sie die `:hover`-Pseudoklasse, um die `transform`-Eigenschaft auf `scale(1.1)` zu ändern. Dadurch wird das Element vergrößert, wenn der Benutzer es mit der Maus überfährt.

Hier ist ein Beispiel-Codeausschnitt, den Sie verwenden können:

```html
<button class="button-grow">Submit</button>
```

```css
.button-grow {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.button-grow:hover {
  transform: scale(1.1);
}
```

Klicken Sie bitte auf 'Go Live' in der unteren rechten Ecke, um den Web-Service auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzusehen.
