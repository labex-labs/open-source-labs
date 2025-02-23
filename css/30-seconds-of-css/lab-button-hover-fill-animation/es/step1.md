# Animación de relleno del botón

`index.html` y `style.css` ya se han proporcionado en la VM.

Para crear una animación de relleno al pasar el cursor, puedes establecer las propiedades `color` y `background` y aplicar una `transición` adecuada para animar los cambios. Para desencadenar la animación al pasar el cursor, utiliza la pseudo-clase `:hover` para cambiar las propiedades `background` y `color` del elemento. Aquí hay un fragmento de código de ejemplo:

```html
<button class="animated-fill-button">Submit</button>
```

```css
.animated-fill-button {
  padding: 20px;
  background: #fff;
  color: #000;
  border: 1px solid #000;
  cursor: pointer;
  transition: 0.3s all ease-in-out;
}

.animated-fill-button:hover {
  background: #000;
  color: #fff;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
