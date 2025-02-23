# Función para Devolver la Diferencia de Dos Arrays por Mapeo

Para comenzar a codificar, abre tu Terminal/SSH y escribe `node`.

Esta función toma dos arrays y aplica la función proporcionada a cada elemento de ambos arrays para devolver su diferencia.

Para hacer esto:

- Crea un `Set` aplicando la función (`fn`) a cada elemento del segundo array (`b`).
- Utiliza `Array.prototype.map()` para aplicar la función (`fn`) a cada elemento del primer array (`a`).
- Utiliza `Array.prototype.filter()` en combinación con la función (`fn`) en el primer array (`a`) para conservar solo los valores no contenidos en el segundo array (`b`), utilizando `Set.prototype.has()`.

Aquí está el código de la función:

```js
const differenceBy = (a, b, fn) => {
  const s = new Set(b.map(fn));
  return a.map(fn).filter((el) => !s.has(el));
};
```

Aquí hay algunos ejemplos de cómo utilizar la función:

```js
differenceBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [1]
differenceBy([{ x: 2 }, { x: 1 }], [{ x: 1 }], (v) => v.x); // [2]
```
