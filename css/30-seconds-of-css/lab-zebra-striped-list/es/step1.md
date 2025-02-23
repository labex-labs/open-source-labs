# Lista con rayas de cebra

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear una lista con colores de fondo alternados, utiliza los selectores pseudo-clase `:nth-child(odd)` o `:nth-child(even)` para aplicar un diferente `background-color` a los elementos según su posición entre los hermanos. Esto se puede aplicar a varios elementos HTML como `<div>`, `<tr>`, `<p>`, `<ol>`, etc.

A continuación, se muestra un ejemplo de cómo crear una lista con rayas con elementos `<li>`:

```html
<ul>
  <li>Item 01</li>
  <li>Item 02</li>
  <li>Item 03</li>
  <li>Item 04</li>
  <li>Item 05</li>
</ul>
```

```css
li:nth-child(odd) {
  background-color: #999;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
