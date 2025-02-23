# Función para rellenar una cadena

Para rellenar una cadena por ambos lados con el carácter especificado, si es más corta que la `length` especificada, utiliza la siguiente función:

```js
const pad = (str, length, char = " ") =>
  str.padStart((str.length + length) / 2, char).padEnd(length, char);
```

La función utiliza `String.prototype.padStart()` y `String.prototype.padEnd()` para rellenar ambos lados de la cadena dada. Puedes omitir el tercer argumento, `char`, para utilizar el carácter de espacio en blanco como el carácter de relleno predeterminado.

A continuación, se presentan algunos ejemplos de cómo utilizar la función `pad()`:

```js
pad("cat", 8); // '  cat   '
pad(String(42), 6, "0"); // '004200'
pad("foobar", 3); // 'foobar'
```

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.
