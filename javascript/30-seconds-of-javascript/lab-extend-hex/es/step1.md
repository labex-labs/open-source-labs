# Cómo extender un código de color de 3 dígitos a un código de color de 6 dígitos

Para practicar la codificación, abre la Terminal/SSH y escribe `node`. Puedes utilizar la siguiente función para extender un código de color de 3 dígitos a un código de color de 6 dígitos:

```js
const extendHex = (shortHex) =>
  "#" +
  shortHex
    .slice(shortHex.startsWith("#") ? 1 : 0)
    .split("")
    .map((x) => x + x)
    .join("");
```

Para convertir un código hexadecimal de color RGB de 3 dígitos a la forma de 6 dígitos, sigue estos pasos:

- Utiliza `Array.prototype.map()`, `String.prototype.split()` y `Array.prototype.join()` para unir la matriz mapeada.
- Utiliza `Array.prototype.slice()` para eliminar `#` del inicio de la cadena ya que se agrega una vez.

Aquí hay algunos ejemplos:

```js
extendHex("#03f"); // '#0033ff'
extendHex("05a"); // '#0055aa'
```
