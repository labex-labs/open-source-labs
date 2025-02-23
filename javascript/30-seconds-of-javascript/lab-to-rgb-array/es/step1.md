# Convertir una cadena RGB en una matriz

Para convertir una cadena de color `rgb()` en una matriz de valores, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `String.prototype.match()` para obtener una matriz de 3 cadenas con los valores numéricos.
3. Utiliza `Array.prototype.map()` en combinación con `Number` para convertirlos en una matriz de valores numéricos.

Aquí está el código que puedes utilizar:

```js
const toRGBArray = (rgbStr) => rgbStr.match(/\d+/g).map(Number);
```

Para probar la función, llámala con una cadena de color `rgb()` como argumento, así:

```js
toRGBArray("rgb(255, 12, 0)"); // [255, 12, 0]
```
