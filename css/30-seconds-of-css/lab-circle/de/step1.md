# Kreis

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine kreisförmige Gestalt mit reinem CSS zu erstellen, verwenden Sie die Eigenschaft `border-radius: 50%`, um die Kanten des Elements zu krümmen. Stellen Sie sicher, dass Sie sowohl `width` als auch `height` auf den gleichen Wert setzen, um einen perfekten Kreis zu gewährleisten. Wenn unterschiedliche Werte verwendet werden, wird stattdessen eine Ellipse erstellt. Hier ist ein Beispielcodeausschnitt:

```html
<div class="circle"></div>
```

```css
.circle {
  border-radius: 50%;
  width: 32px;
  height: 32px;
  background: #9c27b0;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
