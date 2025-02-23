# Diferencia de arrays

Para encontrar la diferencia entre dos arrays, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a codificar.

2. Crea un `Set` a partir del array `b` para extraer los valores únicos de `b`.

3. Utiliza `Array.prototype.filter()` en el array `a` para conservar solo los valores que no están en el array `b`, utilizando `Set.prototype.has()`.

Aquí está el código:

```js
const difference = (a, b) => {
  const s = new Set(b);
  return a.filter((x) => !s.has(x));
};
```

Uso de ejemplo:

```js
difference([1, 2, 3, 3], [1, 2, 4]); // Salida: [3, 3]
```
