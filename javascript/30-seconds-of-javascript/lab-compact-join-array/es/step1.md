# Aquí hay un consejo sobre cómo Compactar y Unir un Array

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

Aquí está cómo eliminar los valores falsy de un array y combinar los valores restantes en una cadena:

- Utiliza `Array.prototype.filter()` para filtrar los valores falsy como `false`, `null`, `0`, `""`, `undefined` y `NaN`.
- Utiliza `Array.prototype.join()` para unir los valores restantes en una cadena.

```js
const compactJoin = (arr, delim = ",") => arr.filter(Boolean).join(delim);
```

Luego llama a la función y pasa un array como argumento:

```js
compactJoin(["a", "", "b", "c"]); // 'a,b,c'
```
