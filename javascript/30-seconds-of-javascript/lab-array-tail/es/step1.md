# Cómo obtener la cola de un array en JavaScript

Para obtener todos los elementos de un array excepto el primero, puedes utilizar el método `Array.prototype.slice()`. Si la longitud del array es mayor que 1, utiliza `slice(1)` para devolver el array sin el primer elemento. En caso contrario, devuelve el array completo.

Si bien es posible la segmentación negativa (como `slice(-4)`) en JavaScript y se segmenta desde el final, aquí utilizamos `slice(1)` porque:

1. Comunicamos claramente nuestra intención de omitir el primer elemento
2. Funciona de manera consistente independientemente de la longitud del array
3. La segmentación negativa requeriría conocer la longitud del array para obtener el mismo resultado

Aquí hay un ejemplo de código:

```js
const tail = (arr) => (arr.length > 1 ? arr.slice(1) : arr);
```

Ahora puedes utilizar la función `tail()` para obtener la cola del array:

```js
tail([1, 2, 3]); // [2, 3]
tail([1]); // [1]
```
