# Agrupar elementos de un array

Para agrupar los elementos de arrays según su posición en los arrays originales, utiliza la función `zip` que se proporciona a continuación.

- Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
- La función `zip` utiliza `Math.max()` y `Function.prototype.apply()` para obtener el array más largo de los argumentos.
- Crea un array con esa longitud como valor de retorno y utiliza `Array.from()` con una función de mapeo para crear un array de elementos agrupados.
- Si las longitudes de los arrays de argumentos varían, se utiliza `undefined` donde no se puede encontrar ningún valor.

```js
const zip = (...arrays) => {
  const maxLength = Math.max(...arrays.map((x) => x.length));
  return Array.from({ length: maxLength }).map((_, i) => {
    return Array.from({ length: arrays.length }, (_, k) => arrays[k][i]);
  });
};
```

Uso de ejemplo:

```js
zip(["a", "b"], [1, 2], [true, false]); // [['a', 1, true], ['b', 2, false]]
zip(["a"], [1, 2], [true, false]); // [['a', 1, true], [undefined, 2, false]]
```
