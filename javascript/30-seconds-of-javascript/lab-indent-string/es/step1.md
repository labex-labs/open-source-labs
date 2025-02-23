# Una función para indentar cadenas en JavaScript

Para agregar sangría a cada línea de una cadena dada, puedes usar la función `indentString()` en JavaScript. Esta función toma tres argumentos: `str`, `count` e `indent`.

- El argumento `str` representa la cadena que quieres indentar.
- El argumento `count` determina cuántas veces quieres indentar cada línea.
- El argumento `indent` es opcional y representa el carácter que quieres usar para la indentación. Si no lo proporcionas, el valor predeterminado es un carácter de espacio en blanco único (`' '`).

Aquí está el código de la función `indentString()`:

```js
const indentString = (str, count, indent = " ") =>
  str.replace(/^/gm, indent.repeat(count));
```

Para usar esta función, simplemente llámala con los argumentos deseados. Aquí hay algunos ejemplos:

```js
indentString("Lorem\nIpsum", 2); // '  Lorem\n  Ipsum'
indentString("Lorem\nIpsum", 2, "_"); // '__Lorem\n__Ipsum'
```

En el primer ejemplo, `indentString('Lorem\nIpsum', 2)` devuelve `'  Lorem\n  Ipsum'`, lo que significa que cada línea de la cadena de entrada ha sido indentada dos veces con caracteres de espacio.

En el segundo ejemplo, `indentString('Lorem\nIpsum', 2, '_')` devuelve `'__Lorem\n__Ipsum'`, lo que significa que cada línea de la cadena de entrada ha sido indentada dos veces con caracteres de subrayado (`'_'`).
