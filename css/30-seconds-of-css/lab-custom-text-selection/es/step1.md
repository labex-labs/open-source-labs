# Selección de texto personalizada

`index.html` y `style.css` ya se han proporcionado en la VM.

Para modificar el estilo del texto seleccionado, utilice el pseudo-seleccionador `::selection`. Aquí hay un fragmento de código de ejemplo para seleccionar y dar estilo al texto dentro de un elemento párrafo:

```html
<p class="custom-text-selection">Selecciona un poco de este texto.</p>
```

```css
::selection {
  background: aquamarine;
  color: black;
}

.custom-text-selection::selection {
  background: deeppink;
  color: white;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
