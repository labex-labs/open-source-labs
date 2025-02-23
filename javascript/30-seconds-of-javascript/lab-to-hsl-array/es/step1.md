# Convertir HSL a Matriz

Para convertir una cadena de color `hsl()` en una matriz de valores, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `String.prototype.match()` para obtener una matriz de 3 cadenas con los valores numéricos.
3. Utilice `Array.prototype.map()` en combinación con `Number` para convertirlos en una matriz de valores numéricos.

Aquí está el código para convertir una cadena de color `hsl()` en una matriz de valores numéricos:

```js
const toHSLArray = (hslStr) => hslStr.match(/\d+/g).map(Number);
```

Uso de ejemplo:

```js
toHSLArray("hsl(50, 10%, 10%)"); // [50, 10, 10]
```
