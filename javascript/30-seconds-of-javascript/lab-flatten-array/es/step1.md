# Cómo aplanar una matriz con JavaScript

Para aplanar una matriz hasta una profundidad especificada en JavaScript, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza la función `flatten` con dos argumentos: `arr` (la matriz que se va a aplanar) y `depth` (el número máximo de niveles anidados que se van a aplanar).
3. Dentro de la función `flatten`, utiliza la recursión para decrementar `depth` en `1` para cada nivel de profundidad.
4. Utiliza `Array.prototype.reduce()` y `Array.prototype.concat()` para fusionar elementos o matrices.
5. Agrega un caso base para cuando `depth` es igual a `1` para detener la recursión.
6. Omite el segundo argumento, `depth`, para aplanar solo hasta una profundidad de `1` (aplanamiento simple).

Aquí está el código de la función `flatten`:

```js
const flatten = (arr, depth = 1) =>
  arr.reduce(
    (a, v) =>
      a.concat(depth > 1 && Array.isArray(v) ? flatten(v, depth - 1) : v),
    []
  );
```

Puedes probar la función `flatten` con los siguientes ejemplos:

```js
flatten([1, [2], 3, 4]); // [1, 2, 3, 4]
flatten([1, [2, [3, [4, 5], 6], 7], 8], 2); // [1, 2, 3, [4, 5], 6, 7, 8]
```
