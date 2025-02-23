# Disposición de mampostería

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear una disposición en estilo mampostería, utilice `.masonry-container` como el contenedor principal y agregue `.masonry-columns` como un contenedor interno en el que se colocarán los elementos `.masonry-brick`. La disposición consta de "ladrillos" que se empalan entre sí, formando una perfecta combinación. El `width` para una disposición vertical y el `height` para una disposición horizontal pueden ser fijos.

Para garantizar que la disposición fluya correctamente, aplique `display: block` a los elementos `.masonry-brick`. Utilice el selector de pseudo-elemento `:first-child` para aplicar un `margin` diferente al primer elemento para tener en cuenta su posición.

Para mayor flexibilidad y respuesta, utilice variables CSS y consultas de medios. El `.masonry-container` tiene variables CSS para el recuento de columnas y el espaciado. El número de columnas está controlado por consultas de medios que especifican diferentes recuentos y anchos de columnas para diferentes tamaños de pantalla.

```html
<div class="masonry-container">
  <div class="masonry-columns">
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1016/384/256"
      alt="Una imagen"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1025/495/330"
      alt="Otra imagen"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1024/192/128"
      alt="Otra imagen"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1028/518/345"
      alt="Una más imagen"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1035/585/390"
      alt="Y otra más"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1074/384/216"
      alt="Última"
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

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
