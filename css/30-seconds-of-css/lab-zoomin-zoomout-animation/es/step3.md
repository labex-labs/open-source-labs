# Creación de la animación con keyframes

Las animaciones CSS funcionan definiendo keyframes (fotogramas clave) que especifican los estilos que un elemento debe tener en varios puntos durante la secuencia de animación. Vamos a crear los keyframes para nuestra animación de acercamiento y alejamiento.

1. Abre nuevamente el archivo `style.css` y agrega el siguiente código al final:

```css
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

2. Entendamos qué hace este código:

   - `@keyframes` es una regla @ de CSS que define las etapas y estilos de una animación
   - `zoom-in-zoom-out` es el nombre que le damos a nuestra animación (haremos referencia a este nombre más adelante)
   - Dentro de los keyframes, definimos lo que sucede en diferentes puntos de la animación:
     - En `0%` (el inicio), el elemento está en su tamaño normal con `scale(1, 1)`
     - En `50%` (a mitad de camino), el elemento crece a 1.5 veces su tamaño con `scale(1.5, 1.5)`
     - En `100%` (el final), el elemento vuelve a su tamaño normal
   - La propiedad `transform` con la función `scale()` cambia el tamaño del elemento

3. Guarda el archivo `style.css` después de agregar estos keyframes.

Los keyframes definen lo que hará nuestra animación, pero aún no la hemos aplicado a nuestro elemento. En el siguiente paso, conectaremos la animación a nuestro cuadro.
