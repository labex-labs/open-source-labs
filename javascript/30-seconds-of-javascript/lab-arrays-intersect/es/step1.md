# Cómo comprobar si dos arrays tienen un elemento común

Para comprobar si dos arrays tienen un elemento común, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Crea un `Set` a partir de `b` para obtener los valores únicos en `b`.
3. Utiliza `Array.prototype.some()` en `a` para comprobar si cualquiera de sus valores está contenido en `b`, utilizando `Set.prototype.has()`.
4. Utiliza la función `intersects` proporcionada a continuación para probar los arrays.

```js
const intersects = (a, b) => {
  const s = new Set(b);
  return [...new Set(a)].some((x) => s.has(x));
};
```

Utiliza la función `intersects` para comprobar si dos arrays se intersecan:

```js
intersects(["a", "b"], ["b", "c"]); // true
intersects(["a", "b"], ["c", "d"]); // false
```

Siguiendo estos pasos y utilizando el código proporcionado, puedes comprobar fácilmente si dos arrays tienen un elemento común.
