# Cómo extraer valores coincidentes de una matriz

Para extraer valores específicos de una matriz usando JavaScript, siga estos pasos:

1. Abra el Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.filter()` y `Array.prototype.includes()` para filtrar los valores que no se necesitan y crear una nueva matriz.
3. Establezca `Array.prototype.length` para mutar la matriz original reiniciando su longitud a `0`.
4. Utilice `Array.prototype.push()` para volver a poblar la matriz original solo con los valores extraídos.
5. Utilice `Array.prototype.push()` para llevar un registro de los valores eliminados en una nueva matriz.

Aquí hay una función de ejemplo que implementa estos pasos:

```js
const pullAtValue = (arr, pullArr) => {
  let removed = [],
    pushToRemove = arr.forEach((v, i) =>
      pullArr.includes(v) ? removed.push(v) : v
    ),
    mutateTo = arr.filter((v, i) => !pullArr.includes(v));
  arr.length = 0;
  mutateTo.forEach((v) => arr.push(v));
  return removed;
};
```

Puede usar esta función para eliminar valores específicos de una matriz y devolver los elementos eliminados de la siguiente manera:

```js
let myArray = ["a", "b", "c", "d"];
let pulled = pullAtValue(myArray, ["b", "d"]);
// myArray = [ 'a', 'c' ], pulled = [ 'b', 'd' ]
```
