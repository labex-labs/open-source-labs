# Función para Encontrar Valores Únicos Invertidos en un Array

Para encontrar todos los valores únicos de un array en función de una función comparadora proporcionada desde la derecha, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.reduceRight()` y `Array.prototype.some()` para crear un array que contenga solo la última aparición única de cada valor, en función de la función comparadora `fn`.
3. La función comparadora toma dos argumentos: los valores de los dos elementos que se están comparando.
4. Aquí está el código para implementar la función:

```js
const uniqueElementsByRight = (arr, fn) =>
  arr.reduceRight((acc, v) => {
    if (!acc.some((x) => fn(v, x))) acc.push(v);
    return acc;
  }, []);
```

5. Utilice el siguiente código para probar la función:

```js
uniqueElementsByRight(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'e' }, { id: 1, value: 'd' }, { id: 2, value: 'c' } ]
```
