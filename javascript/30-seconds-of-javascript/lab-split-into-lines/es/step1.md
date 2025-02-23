# Cómo comenzar a practicar la programación en Terminal/SSH

Para comenzar a practicar la programación en Terminal/SSH, simplemente escribe `node`.

# Dividir una cadena de texto de varias líneas en una matriz de líneas

Para dividir una cadena de texto de varias líneas en una matriz de líneas:

- Utiliza `String.prototype.split()` y una expresión regular para coincidir con los saltos de línea y crear una matriz.
- La expresión regular `/\r?\n/` coincide con los saltos de línea `\r` y `\n`.
- Esto devolverá una matriz de líneas.

```js
const splitLines = (str) => str.split(/\r?\n/);
```

```js
splitLines("This\nis a\nmultiline\nstring.\n");
// ['This', 'is a','multiline','string.', '']
```
