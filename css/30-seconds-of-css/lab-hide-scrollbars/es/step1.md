# Ocultar barras de desplazamiento

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para permitir que un elemento sea desplazable mientras se ocultan las barras de desplazamiento, siga estos pasos:

- Utilice `overflow: auto` para habilitar el desplazamiento en el elemento.
- Utilice `scrollbar-width: none` para ocultar las barras de desplazamiento en Firefox.
- Utilice `display: none` en el pseudo-elemento `::-webkit-scrollbar` para ocultar las barras de desplazamiento en los navegadores WebKit (como Chrome, Edge y Safari).

A continuación, se muestra una implementación de ejemplo:

```html
<div class="scrollable">
  <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum id
    leo a consectetur. Integer justo magna, ultricies vel enim vitae, egestas
    efficitur leo. Ut nulla orci, rutrum eu augue sed, tempus pellentesque quam.
  </p>
</div>
```

```css
.scrollable {
  width: 200px;
  height: 100px;
  overflow: auto;
  scrollbar-width: none;
}

/* Ocultar barras de desplazamiento en los navegadores WebKit */
.scrollable::-webkit-scrollbar {
  display: none;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
