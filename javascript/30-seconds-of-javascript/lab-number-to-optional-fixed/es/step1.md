# Convertir números a notación de punto fijo

Para convertir un número a notación de punto fijo sin ceros finales, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Number.prototype.toFixed()` para convertir el número en una cadena de notación de punto fijo.
3. Utilice `Number.parseFloat()` para convertir la cadena de notación de punto fijo de nuevo en un número, eliminando los ceros finales.
4. Utilice una literal de plantilla para convertir el número en una cadena.

Código de ejemplo:

```js
const toOptionalFixed = (num, digits) =>
  `${Number.parseFloat(num.toFixed(digits))}`;
```

Puede probar la función con diferentes entradas:

```js
toOptionalFixed(1, 2); // '1'
toOptionalFixed(1.001, 2); // '1'
toOptionalFixed(1.5, 2); // '1.5'
```
