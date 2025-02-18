# Animación de Acercar y Alejar

`index.html` y `style.css` ya se han proporcionado en la máquina virtual (VM).

Para crear una animación de acercar y alejar, sigue estos pasos:

1. Define una animación de tres pasos utilizando `@keyframes`. En el `0%` y el `100%`, establece el elemento en su tamaño original utilizando `scale(1,1)`. En el `50%`, aumenta su tamaño a 1.5 veces su tamaño original utilizando `scale(1.5,1.5)`.

2. Da un tamaño específico al elemento utilizando `width` y `height`.

3. Utiliza `animation` para establecer los valores adecuados para el elemento y hacerlo animado.

Aquí tienes un ejemplo de código HTML y CSS:

```html
<div class="zoom-in-out-box"></div>
```

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 1s ease infinite;
}

@keyframes zoom-in-zoom-out {
  0% {
    transform: scale(1, 1);
  }
  50% {
    transform: scale(1.5, 1.5);
  }
  100% {
    transform: scale(1, 1);
  }
}
```

Haz clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puedes actualizar la pestaña **Web 8080** para previsualizar la página web.
