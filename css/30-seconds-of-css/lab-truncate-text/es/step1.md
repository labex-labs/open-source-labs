# Truncar texto

Se ha proporcionado ya `index.html` y `style.css` en la máquina virtual.

Para truncar texto que es más largo que una línea y agregar una elipsis al final, utiliza las siguientes propiedades CSS:

- `overflow: hidden` para evitar que el texto desborde sus dimensiones
- `white-space: nowrap` para evitar que el texto exceda una línea en altura
- `text-overflow: ellipsis` para agregar una elipsis si el texto excede sus dimensiones
- Especifica un `width` fijo para el elemento para saber cuándo mostrar una elipsis

Tenga en cuenta que este método solo funciona para elementos de una sola línea. Por ejemplo:

```html
<p class="truncate-text">If I exceed one line's width, I will be truncated.</p>
```

```css
.truncate-text {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  width: 200px;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
