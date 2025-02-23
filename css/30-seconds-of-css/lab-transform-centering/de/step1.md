# Zentrierung mit Transforms

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um ein Kind-Element innerhalb seines Eltern-Elements sowohl vertikal als auch horizontal zu zentrieren, folgen Sie diesen Schritten:

1. Setzen Sie die `position`-Eigenschaft des Eltern-Elements auf `relative` und die des Kind-Elements auf `absolute`, um es relativ zu seinem Eltern-Element zu positionieren.
2. Verwenden Sie `left: 50%` und `top: 50%`, um das Kind-Element um 50% von der linken und oberen Kante des Eltern-Elements zu verschieben.
3. Verwenden Sie `transform: translate(-50%, -50%)`, um seine Position zu negieren, so dass es sowohl vertikal als auch horizontal zentriert ist.
4. Beachten Sie, dass die feste `height` und `width` des Eltern-Elements nur zu Demonstrationszwecken sind.

Hier ist ein Beispiel für HTML-Code:

```html
<div class="parent">
  <div class="child">Zentrierter Inhalt</div>
</div>
```

Und hier ist der entsprechende CSS-Code:

```css
.parent {
  border: 1px solid #9c27b0;
  height: 250px;
  position: relative;
  width: 250px;
}

.child {
  left: 50%;
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
