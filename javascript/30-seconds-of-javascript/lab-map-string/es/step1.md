# Función para mapear caracteres en una cadena

Para usar esta función para mapear caracteres en una cadena, siga estos pasos:

- Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
- Utilice `String.prototype.split()` y `Array.prototype.map()` para llamar a la función proporcionada, `fn`, para cada carácter en la cadena dada.
- Utilice `Array.prototype.join()` para recombinar la matriz de caracteres en una nueva cadena.
- La función de devolución de llamada, `fn`, toma tres argumentos: el carácter actual, el índice del carácter actual y la cadena en la que se llamó a `mapString`.

Aquí está el código de la función:

```js
const mapString = (str, fn) =>
  str
    .split("")
    .map((c, i) => fn(c, i, str))
    .join("");
```

Uso de ejemplo:

```js
mapString("lorem ipsum", (c) => c.toUpperCase()); // 'LOREM IPSUM'
```
