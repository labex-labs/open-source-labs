# Comprobando el contenido igual en arrays

Para comprobar si dos arrays contienen los mismos elementos, independientemente del orden, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node`.
2. Utilice un bucle `for...of` sobre un `Set` creado a partir de los valores de ambos arrays.
3. Utilice `Array.prototype.filter()` para comparar la cantidad de ocurrencias de cada valor distinto en ambos arrays.
4. Devuelva `false` si las cantidades no coinciden para ningún elemento, `true` en caso contrario.

Aquí está el código correspondiente:

```js
const haveSameContents = (a, b) => {
  for (const v of new Set([...a, ...b]))
    if (a.filter((e) => e === v).length !== b.filter((e) => e === v).length)
      return false;
  return true;
};
```

Para probar la función, utilice el siguiente código:

```js
haveSameContents([1, 2, 4], [2, 4, 1]); // true
```
