# Image Overlay beim Hovern

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um einen Image-Overlay-Effekt beim Hovern anzuzeigen, folgen Sie diesen Schritten:

1. Verwenden Sie die Pseudoelemente `::before` und `::after` für die oberen und unteren Balken des Overlays. Legen Sie ihre `Opacity`, `Transform` und `Transition` fest, um den gewünschten Effekt zu erzielen.
2. Verwenden Sie `<figcaption>` für den Text des Overlays. Legen Sie `display: flex`, `flex-direction: column` und `justify-content: center` fest, um den Text in das Bild zu zentrieren.
3. Verwenden Sie den Pseudoselektor `:hover`, um die `Opacity` und `Transform` aller Elemente zu aktualisieren und den Overlay anzuzeigen.

Hier ist der zu verwendende HTML-Code:

```html
<figure class="hover-img">
  <img src="https://picsum.photos/id/200/440/320.jpg" />
  <figcaption>
    <h3>Lorem <br />Ipsum</h3>
  </figcaption>
</figure>
```

Und hier ist der zu verwendende CSS-Code:

```css
.hover-img {
  display: inline-block;
  margin: 8px;
  width: 100%;
  max-width: 320px;
  min-width: 240px;
  overflow: hidden;
  position: relative;
  text-align: center;
  background-color: #000;
  color: #fff;
}

.hover-img * {
  box-sizing: border-box;
  transition: all 0.45s ease;
}

.hover-img::before,
.hover-img::after {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.5);
  border-top: 32px solid rgba(0, 0, 0, 0.5);
  border-bottom: 32px solid rgba(0, 0, 0, 0.5);
  z-index: 1;
  opacity: 0;
  transform: scaleY(2);
  transition: all 0.3s ease;
}

.hover-img::before {
  content: "";
  top: 0;
  bottom: auto;
}

.hover-img img {
  vertical-align: top;
  max-width: 100%;
  backface-visibility: hidden;
}

.hover-img figcaption {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  align-items: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  line-height: 1.1em;
  opacity: 0;
  z-index: 2;
  transition-delay: 0.1s;
  font-size: 24px;
  font-family: sans-serif;
  font-weight: 400;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.hover-img:hover::before,
.hover-img:hover::after {
  transform: scale(1);
  opacity: 1;
}

.hover-img:hover img {
  opacity: 0.7;
}

.hover-img:hover figcaption {
  opacity: 1;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
