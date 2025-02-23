# Cómo encadenar funciones asíncronas en JavaScript

Para comenzar a practicar la programación con JavaScript, abre la Terminal/SSH y escribe `node`. Una vez que estés familiarizado con los conceptos básicos, puedes comenzar a trabajar con funciones asíncronas.

La función `pipeAsyncFunctions` te permite realizar la composición de funciones de izquierda a derecha con funciones asíncronas. Aquí es cómo funciona:

- La función acepta cualquier cantidad de funciones asíncronas como argumentos.
- El operador de propagación (`...`) se utiliza para pasar estas funciones como argumentos separados a la función `pipeAsyncFunctions`.
- La función resultante puede aceptar cualquier cantidad de argumentos, pero cada una de las funciones que se componen debe aceptar un solo argumento.
- Las funciones pueden devolver una combinación de valores normales, Promises o ser `async` y devolver a través de `await`.
- El método `reduce()` se utiliza junto con `Promise.prototype.then()` para realizar la composición de funciones.
- El método `reduce()` itera sobre las funciones, ejecutándolas secuencialmente y pasando el resultado de una función a la siguiente.
- Se devuelve la Promise resultante.

Aquí hay un ejemplo de cómo utilizar `pipeAsyncFunctions` para sumar un número:

```js
const sum = pipeAsyncFunctions(
  (x) => x + 1,
  (x) => new Promise((resolve) => setTimeout(() => resolve(x + 2), 1000)),
  (x) => x + 3,
  async (x) => (await x) + 4
);
(async () => {
  console.log(await sum(5)); // 15 (después de un segundo)
})();
```

En este ejemplo, `sum` está compuesto por cuatro funciones que suman diferentes valores al número de entrada. El valor final de `sum` es el resultado de ejecutar cada función secuencialmente, con una demora de un segundo para la segunda función. La palabra clave `async` se utiliza con la última función para permitir el uso de `await`.

Al utilizar `pipeAsyncFunctions`, puedes fácilmente componer cualquier cantidad de funciones asíncronas para crear una funcionalidad más compleja.
