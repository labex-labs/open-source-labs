# Colorear texto

Para imprimir texto coloreado en la consola, sigue los siguientes pasos para utilizar la función `colorize()`:

- Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
- Utiliza literales de plantilla y caracteres especiales para agregar el código de color adecuado a la salida de cadena.
- Para agregar un color de fondo, incluye un carácter especial que restablece el color de fondo al final de la cadena.

La función `colorize()` crea un objeto con 16 propiedades, incluyendo los códigos de color para negro, rojo, verde, amarillo, azul, magenta, cian y blanco. Además, tiene propiedades para agregar un color de fondo al texto.

Para utilizar la función `colorize()`, llámala con el texto que quieres colorear como argumento(s), seguido de la propiedad de color o color de fondo. Por ejemplo, `colorize('foo').red` imprimirá 'foo' con letras rojas.

Utiliza la función `console.log()` para imprimir el texto coloreado en la consola.

```js
const colorize = (...args) => ({
  black: `\x1b[30m${args.join(" ")}`,
  red: `\x1b[31m${args.join(" ")}`,
  green: `\x1b[32m${args.join(" ")}`,
  yellow: `\x1b[33m${args.join(" ")}`,
  blue: `\x1b[34m${args.join(" ")}`,
  magenta: `\x1b[35m${args.join(" ")}`,
  cyan: `\x1b[36m${args.join(" ")}`,
  white: `\x1b[37m${args.join(" ")}`,
  bgBlack: `\x1b[40m${args.join(" ")}\x1b[0m`,
  bgRed: `\x1b[41m${args.join(" ")}\x1b[0m`,
  bgGreen: `\x1b[42m${args.join(" ")}\x1b[0m`,
  bgYellow: `\x1b[43m${args.join(" ")}\x1b[0m`,
  bgBlue: `\x1b[44m${args.join(" ")}\x1b[0m`,
  bgMagenta: `\x1b[45m${args.join(" ")}\x1b[0m`,
  bgCyan: `\x1b[46m${args.join(" ")}\x1b[0m`,
  bgWhite: `\x1b[47m${args.join(" ")}\x1b[0m`
});
```

```js
console.log(colorize("foo").red); // 'foo' (letras rojas)
console.log(colorize("foo", "bar").bgBlue); // 'foo bar' (fondo azul)
console.log(colorize(colorize("foo").yellow, colorize("foo").green).bgWhite);
// 'foo bar' (la primera palabra con letras amarillas, la segunda palabra con letras verdes, fondo blanco para ambas)
```
