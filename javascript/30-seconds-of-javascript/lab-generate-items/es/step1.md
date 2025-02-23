# Práctica de código

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`. Luego, puedes utilizar la función `generateItems` para generar un array con un número específico de elementos.

- Llama a `generateItems` con el número deseado de elementos y una función que se utilizará para generar los elementos.
- `generateItems` utiliza `Array.from()` para crear un array vacío de la longitud especificada, y llama a la función proporcionada con el índice de cada elemento recién creado.
- La función proporcionada toma un argumento: el índice de cada elemento.

```js
const generateItems = (n, fn) => Array.from({ length: n }, (_, i) => fn(i));
```

Aquí hay un ejemplo de cómo utilizar `generateItems` para generar un array de 10 números aleatorios:

```js
generateItems(10, Math.random);
// [0.21, 0.08, 0.40, 0.96, 0.96, 0.24, 0.19, 0.96, 0.42, 0.70]
```
