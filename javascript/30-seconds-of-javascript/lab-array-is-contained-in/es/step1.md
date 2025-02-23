# Función para comprobar si una matriz está contenida en otra matriz

Para comenzar a codificar, abre la Terminal/SSH y escribe `node`. Esta función comprueba si todos los elementos de la primera matriz están presentes en la segunda matriz, independientemente de su orden.

A continuación, se presentan los pasos a seguir:

1. Utiliza un bucle `for...of` para iterar sobre un `Set` creado a partir de la primera matriz.
2. Aplica `Array.prototype.some()` para verificar si todos los valores únicos están presentes en la segunda matriz.
3. Utiliza `Array.prototype.filter()` para comparar la cantidad de ocurrencias de cada valor único en ambas matrices.
4. Si la cantidad de cualquier elemento es mayor en la primera matriz que en la segunda, devuelve `false`. Si no, devuelve `true`.

Echa un vistazo al código siguiente para ver cómo funciona:

```js
const isContainedIn = (a, b) => {
  for (const v of new Set(a)) {
    if (
      !b.some((e) => e === v) ||
      a.filter((e) => e === v).length > b.filter((e) => e === v).length
    )
      return false;
  }
  return true;
};
```

Para probar la función, utiliza el siguiente código:

```js
isContainedIn([1, 4], [2, 4, 1]); // true
```
