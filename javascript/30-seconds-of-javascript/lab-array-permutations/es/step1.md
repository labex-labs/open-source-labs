# Cómo Generar Todas las Permutaciones de un Array

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

Aquí hay un algoritmo que genera todas las permutaciones de los elementos de un array (incluso si contiene duplicados). Sigue estos pasos para implementarlo:

1. Utiliza la recursión.
2. Para cada elemento en el array dado, crea todas las permutaciones parciales para el resto de sus elementos.
3. Utiliza `Array.prototype.map()` para combinar el elemento con cada permutación parcial, luego `Array.prototype.reduce()` para combinar todas las permutaciones en un solo array.
4. Los casos base son para arrays con una longitud de `2` o `1`.
5. Tien cuidado de que el tiempo de ejecución de esta función aumenta exponencialmente con cada elemento del array. Cualquier cosa más de 8 a 10 entradas puede causar que tu navegador se atasque mientras intenta resolver todas las combinaciones diferentes.

Aquí está el código:

```js
const permutations = (arr) => {
  if (arr.length <= 2) return arr.length === 2 ? [arr, [arr[1], arr[0]]] : arr;
  return arr.reduce(
    (acc, item, i) =>
      acc.concat(
        permutations([...arr.slice(0, i), ...arr.slice(i + 1)]).map((val) => [
          item,
          ...val
        ])
      ),
    []
  );
};
```

Puedes probar el código llamando a la función `permutations()` con un argumento de array:

```js
permutations([1, 33, 5]);
// [ [1, 33, 5], [1, 5, 33], [33, 1, 5], [33, 5, 1], [5, 1, 33], [5, 33, 1] ]
```
