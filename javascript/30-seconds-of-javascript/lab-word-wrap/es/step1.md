# Instrucciones para envolver una cadena de texto

Para practicar la codificación, abre la Terminal/SSH y escribe `node`.

Este código envuelve una cadena a un número dado de caracteres utilizando un carácter de ruptura de línea. Para utilizarlo, sigue estos pasos:

1. Utiliza `String.prototype.replace()` y una expresión regular para insertar un carácter de ruptura dado en el espacio en blanco más cercano de `max` caracteres.
2. Si no quieres utilizar el valor predeterminado de `'\n'` para el tercer argumento, `br`, puedes omitirlo y proporcionar tu propio carácter.

Aquí está el código:

```js
const wordWrap = (str, max, br = "\n") =>
  str.replace(
    new RegExp(`(?![^\\n]{1,${max}}$)([^\\n]{1,${max}})\\s`, "g"),
    "$1" + br
  );
```

Y aquí hay algunos ejemplos de cómo utilizarlo:

```js
wordWrap(
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempus.",
  32
);
// 'Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nFusce tempus.'

wordWrap(
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempus.",
  32,
  "\r\n"
);
// 'Lorem ipsum dolor sit amet,\r\nconsectetur adipiscing elit.\r\nFusce tempus.'
```
