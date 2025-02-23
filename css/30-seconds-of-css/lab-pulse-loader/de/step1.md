# Puls-Lader

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine Puls-Effekt-Ladeanimation mit der Eigenschaft `animation-delay` zu erstellen, folgen Sie diesen Schritten:

1. Verwenden Sie `@keyframes`, um eine Animation für zwei `<div>`-Elemente zu definieren. Setzen Sie den Startpunkt (`0%`) für beide Elemente, sodass sie keine `width` oder `height` haben und sich in der Mitte befinden. Für den Endpunkt (`100%`) sollen beide Elemente in `width` und `height` zunehmen, aber ihre `position` zurücksetzen auf `0`.
2. Verwenden Sie `opacity`, um von `1` auf `0` zu übergehen, wenn die Animation abläuft, um den `<div>`-Elementen einen Verschwindungseffekt zu verleihen, wenn sie sich erweitern.
3. Setzen Sie eine vorgegebene `width` und `height` für den übergeordneten Container, `.ripple-loader`. Verwenden Sie `position: relative`, um seine Kinder zu positionieren.
4. Verwenden Sie `animation-delay` auf dem zweiten `<div>`-Element, sodass jedes Element seine Animation zu einem anderen Zeitpunkt startet.

Hier ist der HTML- und CSS-Code, um dies zu erreichen:

```html
<div class="ripple-loader">
  <div></div>
  <div></div>
</div>
```

```css
.ripple-loader {
  position: relative;
  width: 64px;
  height: 64px;
}

.ripple-loader div {
  position: absolute;
  border: 4px solid #454ade;
  border-radius: 50%;
  animation: ripple-loader 1s ease-out infinite;
}

.ripple-loader div:nth-child(2) {
  animation-delay: -0.5s;
}

@keyframes ripple-loader {
  0% {
    top: 32px;
    left: 32px;
    width: 0;
    height: 0;
    opacity: 1;
  }
  100% {
    top: 0;
    left: 0;
    width: 64px;
    height: 64px;
    opacity: 0;
  }
}
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
