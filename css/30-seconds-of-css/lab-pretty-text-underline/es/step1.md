# Subrayado de texto bonito

`index.html` y `style.css` ya se han proporcionado en la VM.

Para evitar que los descensores recorten el subrayado, use `text-shadow` con cuatro valores para crear una sombra gruesa que cubra la línea donde los descensores se encuentran con el subrayado. Asegúrese de que el color de `text-shadow` coincida con el color de `background` y ajuste los valores en `px` para fuentes más grandes. Cree el subrayado real utilizando `background-image` con `linear-gradient()` y `currentColor`. Establezca `background-position`, `background-repeat` y `background-size` para colocar el degradado en la posición correcta. Utilice el selector de pseudo-clase `::selection` para asegurarse de que la sombra de texto no interfiera con la selección de texto. Tenga en cuenta que este efecto se implementa nativamente como `text-decoration-skip-ink: auto`, pero tiene menos control sobre el subrayado.

Aquí hay un fragmento de código de ejemplo:

```html
<div class="container">
  <p class="pretty-text-underline">
    Pretty text underline without clipping descenders.
  </p>
</div>
```

```css
.container {
  background: #f5f6f9;
  color: #333;
  padding: 8px 0;
}

.pretty-text-underline {
  display: inline;
  text-shadow:
    1px 1px #f5f6f9,
    -1px 1px #f5f6f9,
    -1px -1px #f5f6f9,
    1px -1px #f5f6f9;
  background-image: linear-gradient(90deg, currentColor 100%, transparent 100%);
  background-position: bottom;
  background-repeat: no-repeat;
  background-size: 100% 1px;
}

.pretty-text-underline::selection {
  background-color: rgba(0, 150, 255, 0.3);
  text-shadow: none;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
