# Poner en Mayúsculas Cada Palabra

Ahora que podemos dividir una cadena de texto (string) en palabras, necesitamos poner en mayúsculas la primera letra de cada palabra y el resto en minúsculas. Implementemos esta funcionalidad.

1. En su sesión de Node.js, escribamos una función para poner en mayúsculas una sola palabra. Escriba:

```javascript
function capitalizeWord(word) {
  return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
}

// Test with a few examples
console.log(capitalizeWord("hello"));
console.log(capitalizeWord("WORLD"));
console.log(capitalizeWord("javaScript"));
```

La salida debería ser:

```
Hello
World
Javascript
```

2. Ahora, apliquemos esta función a una matriz (array) de palabras utilizando el método `map()`. Escriba:

```javascript
let words = ["hello", "WORLD", "javaScript"];
let capitalizedWords = words.map((word) => capitalizeWord(word));
console.log(capitalizedWords);
```

La salida debería ser:

```
[ 'Hello', 'World', 'Javascript' ]
```

El método `map()` crea una nueva matriz (array) aplicando una función a cada elemento de la matriz original. En este caso, estamos aplicando nuestra función `capitalizeWord` a cada palabra.

3. Finalmente, unamos las palabras en mayúsculas para formar una cadena de texto en Pascal Case:

```javascript
let pascalCase = capitalizedWords.join("");
console.log(pascalCase);
```

La salida debería ser:

```
HelloWorldJavascript
```

El método `join("")` combina todos los elementos de una matriz (array) en una sola cadena de texto, utilizando el delimitador proporcionado (una cadena vacía en este caso) entre cada elemento.

Estos pasos demuestran el proceso central de convertir una cadena de texto a Pascal Case:

1. Dividir la cadena de texto en palabras.
2. Poner en mayúsculas cada palabra.
3. Unir las palabras sin ningún separador.
