# Crear el primer gradiente

Ahora comenzaremos a crear nuestro patrón de tablero de ajedrez utilizando gradientes CSS. Vamos a agregar el primer gradiente lineal para crear parte del patrón.

## Comprender los gradientes lineales CSS

Los gradientes lineales CSS te permiten crear transiciones suaves entre dos o más colores en una línea recta. La función `linear-gradient()` toma un ángulo y una serie de puntos de parada de color como parámetros. Utilizaremos esta técnica para crear los cuadrados de nuestro tablero de ajedrez.

Sigue estos pasos:

1. Abre el archivo `style.css`.

2. Modifiquemos nuestra clase `.checkerboard` para incluir el primer gradiente lineal:

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
  );
  background-size: 60px 60px;
}
```

Permíteme explicar lo que hace este gradiente:

- `45deg` especifica el ángulo del gradiente.
- `#000 25%` crea un color negro desde el 0% hasta el 25% del espacio disponible.
- `transparent 25%` crea un color transparente a partir del 25%.
- `transparent 75%` mantiene el color transparente hasta el 75%.
- `#000 75%` vuelve a cambiar a negro en el 75% y continúa hasta el final.
- `background-size: 60px 60px` establece el tamaño de cada celda de gradiente repetida.

3. Guarda el archivo `style.css`.

4. Refresca la pestaña **Web 8080** para ver los cambios.

Ahora deberías ver un patrón comenzando a formarse, pero aún no es un tablero de ajedrez completo. El primer gradiente crea solo una parte del patrón. En el siguiente paso, agregaremos un segundo gradiente para completar el tablero de ajedrez.
