# Springender Ladebalken

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine springende Ladeanimation zu erstellen:

1. Definieren Sie eine `@keyframes`-Animation, die die `opacity`- und `transform`-Eigenschaften verwendet, mit einer Translation auf einer einzelnen Achse bei `transform: translate3d()` für eine bessere Leistung.
2. Erstellen Sie einen Elterncontainer mit der Klasse `.bouncing-loader`, der `display: flex` und `justify-content: center` verwendet, um die springenden Kreise zentriert zu positionieren.
3. Geben Sie den drei `<div>`-Elementen für die springenden Kreise die gleiche `width`, `height` und `border-radius: 50%`, um sie kreisförmig zu gestalten.
4. Wenden Sie die `bouncing-loader`-Animation auf jeden der drei springenden Kreise an.
5. Verwenden Sie für jeden Kreis eine unterschiedliche `animation-delay` und `animation-direction: alternate`, um das gewünschte Ergebnis zu erzielen.

Hier ist der HTML-Code:

```html
<div class="bouncing-loader">
  <div></div>
  <div></div>
  <div></div>
</div>
```

Und hier ist der CSS-Code:

```css
@keyframes bouncing-loader {
  to {
    opacity: 0.1;
    transform: translate3d(0, -16px, 0);
  }
}

.bouncing-loader {
  display: flex;
  justify-content: center;
}

.bouncing-loader > div {
  width: 16px;
  height: 16px;
  margin: 3rem 0.2rem;
  background: #8385aa;
  border-radius: 50%;
  animation: bouncing-loader 0.6s infinite alternate;
}

.bouncing-loader > div:nth-child(2) {
  animation-delay: 0.2s;
}

.bouncing-loader > div:nth-child(3) {
  animation-delay: 0.4s;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
