# Completar el patrón de tablero de ajedrez

Ahora agreguemos el segundo gradiente lineal para completar nuestro patrón de tablero de ajedrez y hacerlo repetible en todo el elemento.

1. Abre nuevamente el archivo `style.css`.

2. Modifica la clase `.checkerboard` para incluir un segundo gradiente lineal que creará el patrón alternado:

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(
      45deg,
      #000 25%,
      transparent 25%,
      transparent 75%,
      #000 75%,
      #000
    ), linear-gradient(-45deg, #000 25%, transparent 25%, transparent 75%, #000
        75%, #000);
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

Lo que hemos agregado:

- Un segundo `linear-gradient()` que es similar al primero pero con un ángulo de `-45deg` para crear el patrón alternado.
- La propiedad `background-repeat: repeat` asegura que los patrones se repitan en todo el elemento.

La combinación de estos dos gradientes en diferentes ángulos crea el clásico patrón de tablero de ajedrez. El primer gradiente crea un conjunto de cuadrados diagonales, mientras que el segundo gradiente crea otro conjunto que llena los espacios en blanco.

3. Guarda el archivo `style.css`.

4. Refresca la pestaña **Web 8080** para ver el resultado final.

Ahora deberías ver un patrón de tablero de ajedrez completo con cuadrados alternados de color negro y blanco. El patrón debe repetirse en todo el elemento de 240px por 240px.

## Cómo funciona el patrón

El efecto de tablero de ajedrez se crea mediante:

1. Utilizar dos gradientes lineales con ángulos opuestos (45deg y -45deg).
2. Cada gradiente crea un patrón de cuadrados negros en las esquinas.
3. Las áreas transparentes permiten que se vea el fondo blanco.
4. La propiedad `background-size` controla el tamaño de cada cuadrado en el patrón.
5. La propiedad `background-repeat` hace que el patrón se repita en todo el elemento.

Esta técnica demuestra el poder de los gradientes CSS para crear patrones complejos sin necesidad de archivos de imagen, lo que resulta en tiempos de carga más rápidos y una mejor escalabilidad.
