# Función de JavaScript para comprobar si una cadena está en minúsculas

Para comprobar si una cadena de texto dada está en minúsculas, puedes utilizar la siguiente función de JavaScript. Primero, convierte la cadena a minúsculas utilizando `String.prototype.toLowerCase()` y luego compárala con la cadena original utilizando la igualdad estricta (`===`).

```js
const isLowerCase = (str) => str === str.toLowerCase();
```

Aquí hay un ejemplo de uso:

```js
isLowerCase("abc"); // true
isLowerCase("a3@$"); // true
isLowerCase("Ab4"); // false
```

Para utilizar esta función, abre la Terminal/SSH y escribe `node`.
