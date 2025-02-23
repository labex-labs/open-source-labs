# Función de JavaScript para Comprobar si una Cadena es un Anagrama

Para comprobar si una cadena es un anagrama de otra cadena, utiliza la siguiente función de JavaScript. Es insensible a mayúsculas y minúsculas y ignora espacios, signos de puntuación y caracteres especiales.

```js
const isAnagram = (str1, str2) => {
  const normalize = (str) =>
    str
      .toLowerCase()
      .replace(/[^a-z0-9]/gi, "")
      .split("")
      .sort()
      .join("");
  return normalize(str1) === normalize(str2);
};
```

Para usar la función, abre la Terminal/SSH y escribe `node`. Luego, llama a la función con dos cadenas como argumentos:

```js
isAnagram("iceman", "cinema"); // true
```

La función utiliza `String.prototype.toLowerCase()` y `String.prototype.replace()` con una expresión regular adecuada para eliminar los caracteres innecesarios. También utiliza `String.prototype.split()`, `Array.prototype.sort()` y `Array.prototype.join()` en ambas cadenas para normalizarlas y comprobar si sus formas normalizadas son iguales.
