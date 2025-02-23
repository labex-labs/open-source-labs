# Función memoizada

Para comenzar a codificar, abre la Terminal/SSH y escribe `node`. Esta función devuelve la función memoizada (almacenada en caché). Aquí están los pasos para utilizar esta función:

1. Instancia un nuevo objeto `Map` para crear una caché vacía.
2. Devuelve una función que toma un solo argumento que se suministrará a la función memoizada. Antes de ejecutar la función, comprueba si la salida para ese valor de entrada específico ya está almacenada en caché. Si es así, devuelve la salida almacenada en caché; de lo contrario, almacénala y devuélvala.
3. Utiliza la palabra clave `function` para permitir que el contexto `this` de la función memoizada se cambie si es necesario.
4. Establece la `cache` como una propiedad en la función devuelta para permitir el acceso a ella.

Aquí está el código que implementa la función memoizada:

```js
const memoize = (fn) => {
  const cache = new Map();
  const cached = function (val) {
    return cache.has(val)
      ? cache.get(val)
      : cache.set(val, fn.call(this, val)) && cache.get(val);
  };
  cached.cache = cache;
  return cached;
};
```

Para ver cómo funciona esta función, puedes utilizarla con la función `anagrams`. Aquí hay un ejemplo:

```js
const anagramsCached = memoize(anagrams);
anagramsCached("javascript"); // Tarda mucho tiempo
anagramsCached("javascript"); // Devuelve virtualmente de inmediato ya que está almacenado en caché
console.log(anagramsCached.cache); // El mapa de anagramas almacenado en caché
```
