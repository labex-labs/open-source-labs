# Práctica de código: Generador de subcadenas izquierda

Para generar todas las subcadenas izquierda de una cadena dada, utiliza la función `leftSubstrGenerator` proporcionada a continuación.

```js
const leftSubstrGenerator = function* (str) {
  if (!str.length) return;
  for (let i in str) yield str.slice(0, i + 1);
};
```

Para utilizar la función, abre la Terminal/SSH y escribe `node`. Luego, ingresa la función con un argumento de cadena:

```js
[...leftSubstrGenerator("hello")];
// [ 'h', 'he', 'hel', 'hell', 'hello' ]
```

La función utiliza `String.prototype.length` para terminar tempranamente si la cadena está vacía y un bucle `for...in` con `String.prototype.slice()` para `yield` cada subcadena de la cadena dada, comenzando por el principio.
