# Fuera de pantalla

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Esta técnica oculta completamente un elemento en el DOM mientras todavía lo hace accesible. Para lograr esto, puedes seguir estos pasos:

- Elimina todos los bordes y relleno y oculta el desbordamiento del elemento.
- Utiliza `clip` para asegurarte de que ninguna parte del elemento se muestre.
- Establece la `altura` y el `ancho` del elemento a `1px` y nega los valores con `margin: -1px`.
- Utiliza `position: absolute` para evitar que el elemento ocupe espacio en el DOM.
- Tenga en cuenta que esta técnica es una mejor alternativa a `display: none` (no legible por los lectores de pantalla) y `visibility: hidden` (ocupa espacio físico en el DOM) en términos de accesibilidad y amigabilidad para el diseño.

Aquí hay un ejemplo de cómo puedes utilizar esta técnica en HTML y CSS:

```html
<a class="button" href="https://google.com">
  Aprende más <span class="offscreen">acerca de pantalones</span>
</a>
```

```css
.offscreen {
  border: 0;
  clip: rect(0 0 0 0);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
