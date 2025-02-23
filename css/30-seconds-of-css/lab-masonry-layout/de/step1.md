# Mauerwerkslayout

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um ein Mauerwerkslayout zu erstellen, verwenden Sie die Klasse `.masonry-container` als Hauptcontainer und fügen Sie die Klasse `.masonry-columns` als inneren Container hinzu, in den die `.masonry-brick`-Elemente platziert werden. Das Layout besteht aus "Ziegelsteinen", die ineinander fallen und perfekt zusammenpassen. Die `width` für ein vertikales Layout und die `height` für ein horizontales Layout können festgelegt werden.

Um sicherzustellen, dass das Layout ordnungsgemäß fließt, wenden Sie `display: block` auf die `.masonry-brick`-Elemente an. Verwenden Sie den `:first-child`-Pseudo-Element-Selektor, um einen anderen `margin` für das erste Element anzuwenden, um seine Positionierung zu berücksichtigen.

Für eine größere Flexibilität und Responsivität verwenden Sie CSS-Variablen und Medienabfragen. Der `.masonry-container` hat CSS-Variablen für die Spaltenanzahl und den Abstand. Die Anzahl der Spalten wird durch Medienabfragen gesteuert, die unterschiedliche Spaltenanzahlen und -breiten für verschiedene Bildschirmgrößen angeben.

```html
<div class="masonry-container">
  <div class="masonry-columns">
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1016/384/256"
      alt="An image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1025/495/330"
      alt="Another image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1024/192/128"
      alt="Another image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1028/518/345"
      alt="One more image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1035/585/390"
      alt="And another one"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1074/384/216"
      alt="Last one"
    />
  </div>
</div>
```

```css
.masonry-container {
  --column-count-small: 1;
  --column-count-medium: 2;
  --column-count-large: 3;
  --column-gap: 0.125rem;
  padding: var(--column-gap);
}

.masonry-columns {
  column-gap: var(--column-gap);
  column-count: var(--column-count-small);
  column-width: calc(1 / var(--column-count-small) * 100%);
}

@media only screen and (min-width: 640px) {
  .masonry-columns {
    column-count: var(--column-count-medium);
    column-width: calc(1 / var(--column-count-medium) * 100%);
  }
}

@media only screen and (min-width: 800px) {
  .masonry-columns {
    column-count: var(--column-count-large);
    column-width: calc(1 / var(--column-count-large) * 100%);
  }
}

.masonry-brick {
  width: 100%;
  height: auto;
  margin: var(--column-gap) 0;
  display: block;
}

.masonry-brick:first-child {
  margin: 0 0 var(--column-gap);
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite zu previewen.
