# Cómo digitalizar un número

Para digitalizar un número en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Math.abs()` para quitar el signo del número.
3. Convierta el número en una cadena y utilice el operador de propagación (`...`) para crear una matriz de dígitos.
4. Utilice `Array.prototype.map()` y `parseInt()` para convertir cada dígito en un entero.

Aquí está el código para la función `digitize`:

```js
const digitize = (n) => [...`${Math.abs(n)}`].map((i) => parseInt(i));
```

Uso de ejemplo:

```js
digitize(123); // [1, 2, 3]
digitize(-123); // [1, 2, 3]
```
