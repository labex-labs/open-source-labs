# Bild beim Hovern rotieren

`index.html` und `style.css` wurden bereits in der VM zur Verfügung gestellt.

Um einen Rotations-Effekt für ein Bild beim Hovern zu erstellen, verwenden Sie die Eigenschaften `scale()`, `rotate()` und `transition`, wenn Sie über das übergeordnete Element (in diesem Fall sollte es ein `<figure>`-Element sein) hov ern. Um sicherzustellen, dass die Bildtransformation nicht über das übergeordnete Element hinausläuft, fügen Sie `overflow: hidden` zur CSS des übergeordneten Elements hinzu. Hier ist ein Beispiel für HTML- und CSS-Code:

```html
<figure class="hover-rotate">
  <img src="https://picsum.photos/id/669/600/800.jpg" />
</figure>
```

```css
.hover-rotate {
  overflow: hidden;
  margin: 8px;
  min-width: 240px;
  max-width: 320px;
  width: 100%;
}

.hover-rotate img {
  transition: all 0.3s;
  box-sizing: border-box;
  max-width: 100%;
}

.hover-rotate:hover img {
  transform: scale(1.3) rotate(5deg);
}
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
