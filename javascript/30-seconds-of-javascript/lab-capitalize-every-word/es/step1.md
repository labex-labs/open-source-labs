# Cómo poner en mayúsculas cada palabra en JavaScript

Para poner en mayúsculas cada palabra de una cadena utilizando JavaScript, puedes utilizar el método `String.prototype.replace()` para coincidir con el primer carácter de cada palabra y luego utilizar el método `String.prototype.toUpperCase()` para ponerlo en mayúsculas.

Aquí hay un fragmento de código de ejemplo que puedes utilizar:

```js
const capitalizeEveryWord = (str) =>
  str.replace(/\b[a-z]/g, (char) => char.toUpperCase());
```

Para utilizar esta función, pasa la cadena que quieres poner en mayúsculas como argumento, así:

```js
capitalizeEveryWord("hello world!"); // 'Hello World!'
```

Esto devolverá la cadena en mayúsculas 'Hello World!'.
