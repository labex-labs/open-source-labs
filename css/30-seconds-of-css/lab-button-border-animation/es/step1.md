# Animación de borde de botón

`index.html` y `style.css` ya se han proporcionado en la VM.

Para crear una animación de borde al pasar el cursor por encima, puedes utilizar los pseudo-elementos `::before` y `::after` para generar dos cajas que tengan un ancho de `24px` y estén posicionadas arriba y abajo de la caja. Luego, aplica la pseudo-clase `:hover` para aumentar el `ancho` de esos elementos a `100%` al pasar el cursor por encima y animar la transición utilizando `transition`.

Aquí hay un fragmento de código de ejemplo:

```html
<button class="animated-border-button">Submit</button>
```

```css
.animated-border-button {
  background-color: #263059;
  border: none;
  color: #ffffff;
  outline: none;
  padding: 12px 40px 10px;
  position: relative;
}

.animated-border-button::before,
.animated-border-button::after {
  border: 0 solid transparent;
  transition: all 0.3s;
  content: "";
  height: 0;
  position: absolute;
  width: 24px;
}

.animated-border-button::before {
  border-top: 2px solid #263059;
  right: 0;
  top: -4px;
}

.animated-border-button::after {
  border-bottom: 2px solid #263059;
  bottom: -4px;
  left: 0;
}

.animated-border-button:hover::before,
.animated-border-button:hover::after {
  width: 100%;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
