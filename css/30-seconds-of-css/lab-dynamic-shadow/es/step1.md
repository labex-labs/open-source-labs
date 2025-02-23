# Sombra dinámica

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear una sombra que se basa en los colores de un elemento, siga estos pasos:

1. Utilice el pseudo-elemento `::after` con `position: absolute` y `width` y `height` establecidos en `100%` para llenar el espacio disponible en el elemento padre.

2. Herede el `background` del elemento padre utilizando `background: inherit`.

3. Desplace ligeramente el pseudo-elemento utilizando `top`. Luego, utilice `filter: blur()` para crear una sombra y establezca `opacity` para que sea semi-transparente.

4. Coloque el pseudo-elemento detrás de su padre estableciendo `z-index: -1`. Establezca `z-index: 1` en el elemento padre.

A continuación, se muestra un ejemplo de código HTML y CSS:

```html
<div class="dynamic-shadow"></div>
```

```css
.dynamic-shadow {
  position: relative;
  width: 10rem;
  height: 10rem;
  background: linear-gradient(75deg, #6d78ff, #00ffb8);
  z-index: 1;
}

.dynamic-shadow::after {
  content: "";
  width: 100%;
  height: 100%;
  position: absolute;
  background: inherit;
  top: 0.5rem;
  filter: blur(0.4rem);
  opacity: 0.7;
  z-index: -1;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
