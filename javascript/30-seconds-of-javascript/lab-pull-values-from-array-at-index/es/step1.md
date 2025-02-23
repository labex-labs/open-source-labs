# Cómo extraer valores de un array en un índice

Para extraer valores específicos de un array en ciertos índices, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.filter()` y `Array.prototype.includes()` para filtrar los valores que no se necesitan y almacénelos en un nuevo array llamado `removed`.
3. Establezca `Array.prototype.length` en `0` para mutar el array original restableciendo su longitud.
4. Utilice `Array.prototype.push()` para volver a poblar el array original solo con los valores extraídos.
5. Utilice `Array.prototype.push()` para llevar un registro de los valores eliminados.
6. La función `pullAtIndex` toma dos argumentos: el array original y un array de índices para extraer.
7. La función devuelve un array de valores eliminados.

Uso de ejemplo:

```js
const pullAtIndex = (arr, pullArr) => {
  let removed = [];
  let pulled = arr
    .map((v, i) => (pullArr.includes(i) ? removed.push(v) : v))
    .filter((v, i) => !pullArr.includes(i));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
  return removed;
};

let myArray = ["a", "b", "c", "d"];
let pulled = pullAtIndex(myArray, [1, 3]);
// myArray = [ 'a', 'c' ], pulled = [ 'b', 'd' ]
```
