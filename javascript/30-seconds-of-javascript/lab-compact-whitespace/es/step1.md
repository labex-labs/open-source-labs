# Función para Compactar Espacios en Blanco en una Cadena

Para compactar los espacios en blanco en una cadena, utiliza la función `compactWhitespace()`.

- Utiliza `String.prototype.replace()` con una expresión regular para reemplazar todas las ocurrencias de 2 o más caracteres de espacio en blanco con un solo espacio.
- La función toma una cadena como argumento y devuelve la cadena compactada.

```js
const compactWhitespace = (str) => str.replace(/\s{2,}/g, " ");
```

Uso de ejemplo:

```js
compactWhitespace("Lorem    Ipsum"); // 'Lorem Ipsum'
compactWhitespace("Lorem \n Ipsum"); // 'Lorem Ipsum'
```
