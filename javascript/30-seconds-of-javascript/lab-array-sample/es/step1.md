# Cómo obtener un elemento aleatorio de un array en JavaScript

Para obtener un elemento aleatorio de un array en JavaScript, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza el método `Math.random()` para generar un número aleatorio entre 0 y 1.
3. Multiplica el número aleatorio por la longitud del array utilizando `Array.prototype.length`.
4. Redondea el resultado al número entero más cercano utilizando `Math.floor()`.
5. Utiliza el número redondeado como índice para acceder a un elemento aleatorio del array.
6. Este método también funciona con cadenas de texto.

A continuación, se muestra un fragmento de código que demuestra este enfoque:

```js
const getRandomElement = (arr) => arr[Math.floor(Math.random() * arr.length)];
```

Puedes utilizar la función `getRandomElement` con cualquier array para obtener un elemento aleatorio. Por ejemplo:

```js
getRandomElement([3, 7, 9, 11]); // 9
```
