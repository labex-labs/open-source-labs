# Dar estilo a enlaces sin texto

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para mostrar la URL del enlace para enlaces que no tienen texto, puedes usar la pseudo-clase `:empty` para seleccionar tales enlaces, la pseudo-clase `:not` para excluir enlaces con texto y la propiedad `content` en combinación con la función `attr()` para mostrar la URL del enlace en el pseudo-elemento `::before`. Aquí hay un fragmento de código de ejemplo:

```html
<a href="https://30secondsofcode.org"></a>
```

```css
a[href^="http"]:empty::before {
  content: attr(href);
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
