# Texto grabado

`index.html` y `style.css` ya se han proporcionado en la VM.

Para crear un efecto "grabado" o tallado en relieve para el texto sobre un fondo, utiliza las siguientes propiedades CSS:

```css
.etched-text {
  text-shadow: 0 2px white;
  font-size: 1.5rem;
  font-weight: bold;
  color: #b8bec5;
}
```

La propiedad `text-shadow` crea una sombra blanca desplazada `0px` horizontalmente y `2px` verticalmente desde la posición de origen. Asegúrate de que el fondo sea más oscuro que la sombra para que el efecto funcione. Además, el color del texto debe estar ligeramente desvanecido para que parezca que ha sido tallado del fondo. Finalmente, aplica la clase `etched-text` al elemento HTML deseado, como un párrafo, para lograr el efecto.

```html
<p class="etched-text">I appear etched into the background.</p>
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
