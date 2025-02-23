# Generador de subcadenas derechos

Para generar todas las subcadenas derechos de una cadena dada, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `String.prototype.length` para detener la iteración tempranamente si la cadena está vacía.
3. Utilice un bucle `for...in` y `String.prototype.slice()` para `generar` cada subcadena de la cadena dada, comenzando desde el final.

Aquí está el fragmento de código:

```js
const rightSubstrGenerator = function* (str) {
  if (!str.length) return;
  for (let i in str) yield str.slice(-i - 1);
};
```

Uso de ejemplo:

```js
[...rightSubstrGenerator("hello")];
// [ 'o', 'lo', 'llo', 'ello', 'hello' ]
```
