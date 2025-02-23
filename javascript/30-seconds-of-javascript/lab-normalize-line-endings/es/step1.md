# Función para normalizar los finales de línea

Para normalizar los finales de línea en una cadena, puedes utilizar la siguiente función.

```js
const normalizeLineEndings = (str, normalized = "\r\n") =>
  str.replace(/\r?\n/g, normalized);
```

- Utiliza `String.prototype.replace()` con una expresión regular para coincidir y reemplazar los finales de línea con la versión `normalizada`.
- Por defecto, la versión `normalizada` se establece en `'\r\n'`.
- Para utilizar una versión `normalizada` diferente, pásala como segundo argumento.

Aquí hay algunos ejemplos:

```js
normalizeLineEndings("This\r\nis a\nmultiline\nstring.\r\n");
// 'This\r\nis a\r\nmultiline\r\nstring.\r\n'

normalizeLineEndings("This\r\nis a\nmultiline\nstring.\r\n", "\n");
// 'This\nis a\nmultiline\nstring.\n'
```
