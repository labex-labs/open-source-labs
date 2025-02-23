# Cambiar la Visibilidad Basada en el Estado de Visibilidad Actual

jQuery también te permite cambiar la visibilidad de un contenido basado en su estado de visibilidad actual. `.toggle()` mostrará el contenido que actualmente está oculto y ocultará el contenido que actualmente es visible. Puedes pasar los mismos argumentos a `.toggle()` que pasas a cualquiera de los métodos de efectos anteriores.

```js
// Alternar instantáneamente la visualización de todos los párrafos
$("p").toggle();

// Alternar la visualización de todos los divs en 1,8 segundos
$("div").toggle(1800);
```

`.toggle()` usará una combinación de efectos de deslizamiento y desvanecimiento, al igual que `.show()` y `.hide()`.

> Puedes actualizar la pestaña **Web 8080** para previsualizar la página web.
