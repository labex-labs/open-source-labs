# ¿Cómo comprobar si una cadena es un palíndromo en JavaScript?

Para comprobar si una cadena dada es un palíndromo en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Normalice la cadena a minúsculas utilizando el método `String.prototype.toLowerCase()`.
3. Quite los caracteres no alfanuméricos de la cadena utilizando el método `String.prototype.replace()` y una expresión regular `[\W_]`.
4. Divida la cadena normalizada en caracteres individuales utilizando el operador de propagación (`...`).
5. Invierta la matriz de caracteres utilizando el método `Array.prototype.reverse()`.
6. Una la matriz de caracteres invertida en una cadena utilizando el método `Array.prototype.join()`.
7. Compare la cadena invertida con la cadena normalizada para determinar si es un palíndromo.

A continuación, se muestra un fragmento de código de ejemplo que implementa los pasos anteriores:

```js
const palindrome = (str) => {
  const normalizedStr = str.toLowerCase().replace(/[\W_]/g, "");
  return normalizedStr === [...normalizedStr].reverse().join("");
};

console.log(palindrome("taco cat")); // true
```

En el ejemplo anterior, la función `palindrome()` toma un argumento de cadena y devuelve `true` si la cadena es un palíndromo, y `false` en caso contrario. La función utiliza los pasos descritos anteriormente para comprobar si la cadena es un palíndromo.
