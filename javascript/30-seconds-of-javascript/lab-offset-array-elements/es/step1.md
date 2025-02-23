# Cómo desplazar elementos de un array en JavaScript

Para mover un número específico de elementos al final de un array de JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `Array.prototype.slice()` dos veces para obtener los elementos después del índice especificado y los elementos anteriores a ese índice.
3. Utilice el operador de propagación (`...`) para combinar los dos arrays en uno solo.
4. Si el `desplazamiento` es negativo, los elementos se moverán desde el final hasta el principio del array.

A continuación, se muestra un fragmento de código de ejemplo que implementa la función `desplazamiento`:

```js
const desplazamiento = (arr, desplazamiento) => [
  ...arr.slice(desplazamiento),
  ...arr.slice(0, desplazamiento)
];
```

Luego, puede llamar a la función con los valores de array y desplazamiento deseados:

```js
desplazamiento([1, 2, 3, 4, 5], 2); // [3, 4, 5, 1, 2]
desplazamiento([1, 2, 3, 4, 5], -2); // [4, 5, 1, 2, 3]
```
