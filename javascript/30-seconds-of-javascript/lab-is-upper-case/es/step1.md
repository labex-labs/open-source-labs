# Función para comprobar si una cadena está en mayúsculas

Para comprobar si una cadena está en mayúsculas, siga estos pasos:

1. Abra la Terminal/SSH.
2. Escriba `node`.
3. Utilice la función `isUpperCase()` para convertir la cadena dada a mayúsculas, utilizando `String.prototype.toUpperCase()`, y compárela con la cadena original.
4. La función devolverá `true` si la cadena está en mayúsculas y `false` si no lo está.

A continuación, se muestra un ejemplo de código:

```js
const isUpperCase = (str) => str === str.toUpperCase();

console.log(isUpperCase("ABC")); // true
console.log(isUpperCase("A3@$")); // true
console.log(isUpperCase("aB4")); // false
```
