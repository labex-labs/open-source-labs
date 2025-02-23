# Deshabilitar la selección

`index.html` y `style.css` ya se han proporcionado en la VM.

Para hacer que el contenido de un elemento no sea seleccionable, agrega la propiedad CSS `user-select: none` al selector. Sin embargo, este método no es completamente seguro para evitar que los usuarios copien contenido.

Ejemplo:

```html
<p>You can select me.</p>
<p class="unselectable">You can't select me!</p>
```

```css
.unselectable {
  user-select: none;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
