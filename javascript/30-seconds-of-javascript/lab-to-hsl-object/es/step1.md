# Conversión de HSL a Objeto

Para convertir una cadena de color `hsl()` en un objeto con los valores numéricos de cada color, siga estos pasos:

- Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
- Utilice `String.prototype.match()` para obtener una matriz de 3 cadenas con los valores numéricos.
- Convierta las cadenas en una matriz de valores numéricos utilizando `Array.prototype.map()` en combinación con `Number`.
- Almacene los valores en variables con nombre utilizando la desestructuración de arrays.
- Cree un objeto adecuado a partir de las variables con nombre.

```js
const toHSLObject = (hslStr) => {
  const [hue, saturation, lightness] = hslStr.match(/\d+/g).map(Number);
  return { hue, saturation, lightness };
};
```

Uso de ejemplo:

```js
toHSLObject("hsl(50, 10%, 10%)"); // { hue: 50, saturation: 10, lightness: 10 }
```
