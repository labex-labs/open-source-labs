# Cómo agrupar una matriz en un objeto

Para agrupar una matriz en un objeto, siga estos pasos:

1. Abra la Terminal o SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `Array.prototype.reduce()` para crear un objeto a partir de las dos matrices.
3. Proporcione una matriz de identificadores de propiedad válidos y una matriz de valores.
4. Si la longitud de la matriz de propiedades es mayor que la matriz de valores, las claves restantes se establecerán en `undefined`.
5. Si la longitud de la matriz de valores es mayor que la matriz de propiedades, los valores restantes se ignorarán.

A continuación, se muestra un fragmento de código de ejemplo que demuestra cómo agrupar una matriz en un objeto:

```js
const zipObject = (props, values) =>
  props.reduce((obj, prop, index) => ((obj[prop] = values[index]), obj), {});

zipObject(["a", "b", "c"], [1, 2]); // {a: 1, b: 2, c: undefined}
zipObject(["a", "b"], [1, 2, 3]); // {a: 1, b: 2}
```
