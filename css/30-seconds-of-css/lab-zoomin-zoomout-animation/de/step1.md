# Zoom-In-Zoom-Out-Animation

`index.html` und `style.css` wurden bereits in der virtuellen Maschine (VM) bereitgestellt.

Um eine Zoom-In-Zoom-Out-Animation zu erstellen, folgen Sie diesen Schritten:

1. Definieren Sie eine dreistufige Animation mit `@keyframes`. Bei `0%` und `100%` setzen Sie das Element auf seine ursprüngliche Größe mit `scale(1,1)`. Bei `50%` skalieren Sie es auf das 1,5-fache seiner ursprünglichen Größe mit `scale(1.5,1.5)`.

2. Geben Sie dem Element eine bestimmte Größe mit `width` und `height`.

3. Verwenden Sie `animation`, um die entsprechenden Werte für das Element festzulegen, damit es animiert wird.

Hier ist ein Beispiel für HTML- und CSS-Code:

```html
<div class="zoom-in-out-box"></div>
```

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 1s ease infinite;
}

@keyframes zoom-in-zoom-out {
  0% {
    transform: scale(1, 1);
  }
  50% {
    transform: scale(1.5, 1.5);
  }
  100% {
    transform: scale(1, 1);
  }
}
```

Klicken Sie bitte auf 'Go Live' in der unteren rechten Ecke, um den Web-Service auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzusehen.
