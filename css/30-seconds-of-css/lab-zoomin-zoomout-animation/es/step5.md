# Experimentar con propiedades de animación

Personalicemos nuestra animación experimentando con diferentes propiedades de animación. Esto te ayudará a entender cómo estas propiedades afectan el comportamiento de la animación.

1. Abre el archivo `style.css` y modifica el selector `.zoom-in-out-box` para probar diferentes propiedades de animación:

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 2s ease-in-out infinite;
  /* Add a slight rotation during the animation */
  border-radius: 10px;
}
```

2. Entendamos lo que cambiamos:

   - Extendimos la duración de la animación a `2s` (2 segundos)
   - Cambiamos la función de temporización a `ease-in-out`, que hace que tanto el inicio como el final de la animación sean suaves
   - Agregamos un `border-radius` de 10px para redondear las esquinas de nuestro cuadro

3. También modifiquemos nuestros keyframes para agregar un efecto de rotación:

```css
@keyframes zoom-in-zoom-out {
  0% {
    transform: scale(1, 1) rotate(0deg);
  }
  50% {
    transform: scale(1.5, 1.5) rotate(45deg);
    background-color: #2196f3;
  }
  100% {
    transform: scale(1, 1) rotate(0deg);
  }
}
```

4. En esta definición actualizada de keyframes:

   - Agregamos una función `rotate()` a la propiedad transform
   - En el 50% de la animación, el elemento ahora gira 45 grados mientras se agranda
   - También cambiamos el color de fondo a azul en el 50% de la animación

5. Guarda el archivo `style.css` después de realizar estos cambios.

6. Actualiza la pestaña **Web 8080** para ver tu animación mejorada.

Tu animación ahora debería ser más lenta (2 segundos por ciclo), tener esquinas redondeadas, rotar mientras se acerca y aleja, y cambiar de color a mitad de la animación. Esto demuestra cómo las animaciones CSS pueden combinar múltiples cambios de propiedades para crear efectos visuales ricos.

Siéntete libre de experimentar más con diferentes propiedades y valores para ver cómo afectan tu animación.
