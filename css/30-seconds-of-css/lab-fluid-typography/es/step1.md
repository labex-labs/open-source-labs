# Tipografía fluida

`index.html` y `style.css` ya se han proporcionado en la VM.

Para crear texto que se ajuste en tamaño en función del ancho del viewport, se puede utilizar CSS. Una forma de hacer esto es utilizar la función `clamp()` para establecer los tamaños de fuente mínimo y máximo. Otra forma es utilizar una fórmula para calcular un valor reactivo para el tamaño de fuente. Aquí hay un ejemplo de elemento HTML con una clase de `fluid-type`:

```html
<p class="fluid-type">Hello World!</p>
```

A continuación, se muestra el código CSS correspondiente que establece el tamaño de fuente para que se ajuste entre `1rem` y `3rem` en función del ancho del viewport:

```css
.fluid-type {
  font-size: clamp(1rem, 8vw - 2rem, 3rem);
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
