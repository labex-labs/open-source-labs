# Cómo rellenar un número en JavaScript

Para rellenar un número en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `String.prototype.padStart()` para rellenar el número a la longitud especificada, después de convertirlo en una cadena.
3. La función `padNumber()` que se muestra a continuación demuestra este enfoque.
4. Pase el número y la longitud deseada como argumentos a la función.
5. La función devuelve el número rellenado como una cadena.

```js
const padNumber = (n, l) => `${n}`.padStart(l, "0");
```

Uso de ejemplo:

```js
padNumber(1234, 6); // '001234'
```
