# Función para Combinar Arrays con una Función de Mapeo Proporcionada

Para comenzar a codificar, abre la Terminal/SSH y escribe `node`.

Esta función devuelve un array de elementos que existen en cualquiera de los dos arrays de entrada, después de aplicar la función de mapeo proporcionada a cada elemento de ambos arrays.

A continuación se describen los pasos para lograr esto:

1. Crea un nuevo `Set` aplicando la función de mapeo a todos los valores del primer array de entrada `a`.
2. Crea otro `Set` que consta de todos los elementos de `b` que no coinciden con ningún valor del `Set` previamente creado cuando se aplica la función de mapeo.
3. Combina los dos sets y conviértelos en un array.
4. Devuelve el array resultante.

A continuación se muestra el código de la función `unionBy`:

```js
const unionBy = (a, b, fn) => {
  const setA = new Set(a.map(fn));
  return Array.from(new Set([...a, ...b.filter((x) => !setA.has(fn(x)))]));
};
```

A continuación se presentan algunos ejemplos de cómo utilizar la función `unionBy`:

```js
unionBy([2.1], [1.2, 2.3], Math.floor); // Salida: [2.1, 1.2]
unionBy([{ id: 1 }, { id: 2 }], [{ id: 2 }, { id: 3 }], (x) => x.id);
// Salida: [{ id: 1 }, { id: 2 }, { id: 3 }]
```
