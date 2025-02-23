# Cómo insertar un valor en un índice específico de una matriz utilizando JavaScript

Para insertar un valor en un índice específico de una matriz utilizando JavaScript, siga estos pasos:

1. Abra el Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `Array.prototype.splice()` con un índice adecuado y un recuento de eliminación de `0`, extendiendo los valores dados para insertarlos.
3. La función `insertAt` toma una matriz, un índice y uno o más valores para insertar después del índice especificado.
4. La función muta la matriz original y devuelve la matriz modificada.

A continuación, se muestra un ejemplo de la función `insertAt` en acción:

```js
const insertAt = (arr, i, ...v) => {
  arr.splice(i + 1, 0, ...v);
  return arr;
};

let myArray = [1, 2, 3, 4];
insertAt(myArray, 2, 5); // myArray = [1, 2, 3, 5, 4]

let otherArray = [2, 10];
insertAt(otherArray, 0, 4, 6, 8); // otherArray = [2, 4, 6, 8, 10]
```

En el ejemplo anterior, la función `insertAt` se utiliza para insertar el valor `5` después del segundo índice de la matriz `myArray`, y para insertar los valores `4`, `6` y `8` después del primer índice de la matriz `otherArray`.
