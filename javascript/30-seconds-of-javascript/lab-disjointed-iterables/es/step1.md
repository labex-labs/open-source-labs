# Comprobación de iterables disjuntos

Para comprobar si dos iterables no tienen valores comunes, puedes usar la función `isDisjoint`.

Aquí está cómo usarlo:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Cree un nuevo objeto `Set` a partir de cada iterable usando el constructor `Set`.
3. Use `Array.prototype.every()` y `Set.prototype.has()` para comprobar que los dos iterables no tienen valores comunes.

```js
const isDisjoint = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...sA].every((v) => !sB.has(v));
};
```

Aquí hay algunos ejemplos:

```js
isDisjoint(new Set([1, 2]), new Set([3, 4])); // true
isDisjoint(new Set([1, 2]), new Set([1, 3])); // false
```
