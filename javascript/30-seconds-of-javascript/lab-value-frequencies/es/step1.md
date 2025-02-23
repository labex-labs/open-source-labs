# Instrucciones para contar las frecuencias de valores

Para contar la frecuencia de valores en una matriz, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `Array.prototype.reduce()` para mapear los valores únicos a las claves de un objeto, sumando a las claves existentes cada vez que se encuentra el mismo valor. Esto creará un objeto con los valores únicos de la matriz como claves y sus frecuencias como valores.
3. El código para esta operación es el siguiente:

```js
const frequencies = (arr) =>
  arr.reduce((a, v) => {
    a[v] = a[v] ? a[v] + 1 : 1;
    return a;
  }, {});
```

4. Para utilizar esta función, llame a `frequencies` con la matriz como argumento. Por ejemplo:

```js
frequencies(["a", "b", "a", "c", "a", "a", "b"]); // { a: 4, b: 2, c: 1 }
frequencies([..."ball"]); // { b: 1, a: 1, l: 2 }
```

Con estas instrucciones, puede contar fácilmente la frecuencia de valores en cualquier matriz dada.
