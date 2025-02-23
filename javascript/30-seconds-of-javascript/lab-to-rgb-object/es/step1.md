# Convertir RGB a Objeto

Para convertir una cadena de color `rgb()` en un objeto con los valores de cada color, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `String.prototype.match()` para obtener una matriz de 3 cadenas con los valores numéricos.
3. Utiliza `Array.prototype.map()` en combinación con `Number` para convertirlos en una matriz de valores numéricos.
4. Utiliza la desestructuración de arrays para almacenar los valores en variables con nombres y crear un objeto adecuado a partir de ellos.

Aquí está el código que puedes utilizar:

```js
const toRGBObject = (rgbStr) => {
  const [red, green, blue] = rgbStr.match(/\d+/g).map(Number);
  return { red, green, blue };
};

toRGBObject("rgb(255, 12, 0)"); // {red: 255, green: 12, blue: 0}
```
