# Relación constante de ancho a altura

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Este fragmento de código asegura que un elemento con ancho variable conservará un valor de altura proporcional. Para lograr esto, aplica `padding-top` en el pseudo-elemento `::before`, haciendo que la altura del elemento sea igual a un porcentaje de su ancho. La proporción de altura a ancho se puede modificar según sea necesario. Por ejemplo, un `padding-top` de `100%` creará un cuadrado responsivo con una relación 1:1. Para utilizar este código, simplemente agrega el siguiente código HTML:

```html
<div class="constant-width-to-height-ratio"></div>
```

Luego, agrega el siguiente código CSS:

```css
.constant-width-to-height-ratio {
  background: #9c27b0;
  width: 50%;
}

.constant-width-to-height-ratio::before {
  content: "";
  padding-top: 100%;
  float: left;
}

.constant-width-to-height-ratio::after {
  content: "";
  display: block;
  clear: both;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
