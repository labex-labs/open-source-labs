# Cómo obtener el último elemento de un array en JavaScript

Para comenzar a codificar, abre la Terminal/SSH y escribe `node`. La siguiente función devuelve el último elemento de un array:

```js
const last = (arr) => (arr && arr.length ? arr[arr.length - 1] : undefined);
```

Para usarlo, debes proporcionar un array como argumento. La función comprueba si el array es verdadero y tiene una propiedad `length`. Si ambas condiciones son verdaderas, calcula el índice del último elemento del array y lo devuelve. En caso contrario, devuelve `undefined`.

Aquí hay algunos ejemplos:

```js
last([1, 2, 3]); // 3
last([]); // undefined
last(null); // undefined
last(undefined); // undefined
```
