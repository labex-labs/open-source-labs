# Inicializar una matriz bidimensional en JavaScript

Para inicializar una matriz bidimensional en JavaScript, puedes utilizar el siguiente código:

```js
const initialize2DArray = (width, height, value = null) => {
  return Array.from({ length: height }).map(() =>
    Array.from({ length: width }).fill(value)
  );
};
```

Este código utiliza `Array.from()` y `Array.prototype.map()` para crear una matriz con `height` filas, donde cada fila es una nueva matriz de longitud `width`. También utiliza `Array.prototype.fill()` para establecer todos los elementos de la matriz al parámetro `value`. Si no se proporciona ningún `value`, el valor predeterminado es `null`.

Puedes llamar a la función de la siguiente manera:

```js
initialize2DArray(2, 2, 0); // [[0, 0], [0, 0]]
```

Esto creará una matriz bidimensional con un ancho de 2, una altura de 2 y todos los valores establecidos en 0.
