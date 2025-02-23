# Explicación de las Funciones Juntas

Para usar la función `juxt`, primero abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación. La función `juxt` toma varias funciones como argumentos y devuelve una función que es la juxtaponición de esas funciones.

Para crear la función `juxt`, utiliza `Array.prototype.map()` para devolver una `fn` que puede tomar un número variable de `args`. Cuando se llama a `fn`, debe devolver una matriz que contiene el resultado de aplicar cada `fn` a los `args`.

Aquí hay una implementación de ejemplo de la función `juxt`:

```js
const juxt =
  (...fns) =>
  (...args) =>
    [...fns].map((fn) => [...args].map(fn));
```

Una vez que hayas definido la función `juxt`, puedes usarla pasando cualquier número de funciones como argumentos, seguidos de cualquier número de argumentos para pasar a esas funciones.

Aquí hay un par de ejemplos de uso de la función `juxt`:

```js
juxt(
  (x) => x + 1,
  (x) => x - 1,
  (x) => x * 10
)(1, 2, 3); // [[2, 3, 4], [0, 1, 2], [10, 20, 30]]
```

```js
juxt(
  (s) => s.length,
  (s) => s.split(" ").join("-")
)("happy coding"); // [[18], ['happy-coding']]
```

En el primer ejemplo, la función `juxt` toma tres funciones como argumentos y devuelve una nueva función. Cuando esa nueva función se llama con los argumentos `1, 2, 3`, aplica cada una de las tres funciones a esos argumentos y devuelve una matriz de matrices que contiene los resultados.

En el segundo ejemplo, la función `juxt` toma dos funciones como argumentos y devuelve una nueva función. Cuando esa nueva función se llama con el argumento `'happy-coding'`, aplica cada una de las dos funciones a ese argumento y devuelve una matriz de matrices que contiene los resultados.
