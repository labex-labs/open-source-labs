# Aplicación de la animación

Ahora que hemos definido nuestros keyframes, necesitamos aplicar la animación a nuestro elemento de cuadro.

1. Abre nuevamente el archivo `style.css` y modifica el selector `.zoom-in-out-box` de la siguiente manera:

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 1s ease infinite;
}
```

2. Entendamos la propiedad de animación que agregamos:

   - `animation` es una propiedad abreviada que establece múltiples propiedades de animación a la vez
   - `zoom-in-zoom-out` es el nombre de nuestra animación de keyframes
   - `1s` especifica que un ciclo de la animación dura 1 segundo
   - `ease` es la función de temporización que hace que la animación comience lentamente, acelere y luego se vuelva lenta de nuevo
   - `infinite` significa que la animación se repetirá para siempre

3. Guarda el archivo `style.css` después de realizar estos cambios.

4. Si el servidor web ya está en funcionamiento, simplemente actualiza la pestaña **Web 8080**. Si no, haz clic en "Go Live" en la esquina inferior derecha para iniciar el servidor y luego abre la pestaña **Web 8080**.

Ahora deberías ver tu cuadrado rosa acercándose y alejándose suavemente en una animación continua. El cuadrado crece hasta alcanzar 1.5 veces su tamaño original y luego se contrae hasta su tamaño normal. Este ciclo se repite infinitamente.
