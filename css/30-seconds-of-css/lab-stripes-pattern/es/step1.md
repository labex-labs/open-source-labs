# Patrón de Fondo de Rayas

`index.html` y `style.css` ya se han proporcionado en la VM.

Este código crea un patrón de rayas verticales sobre un fondo blanco.

Para crear el patrón:

- Establece la propiedad `background-color` en blanco.
- Utiliza `background-image` con un valor de `linear-gradient()` para crear una raya vertical.
- Establece la propiedad `background-size` para especificar el tamaño de cada raya.
- Establece `background-repeat` en `repeat` para permitir que el patrón llene el elemento.

Tenga en cuenta que el ancho y alto fijos del elemento son solo para fines de demostración.

Aquí hay un fragmento de código de ejemplo:

```html
<div class="stripes"></div>
```

```css
.stripes {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(90deg, transparent 50%, #000 50%);
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
