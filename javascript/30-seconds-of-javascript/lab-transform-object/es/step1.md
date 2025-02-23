# Transformación de Objetos

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

La función `transform` aplica una función especificada contra un acumulador y cada clave en el objeto, de izquierda a derecha. Aquí está cómo se utiliza:

- Utiliza `Object.keys()` para iterar sobre cada clave en el objeto.
- Utiliza `Array.prototype.reduce()` para aplicar la función especificada contra el acumulador dado.

```js
const transform = (obj, fn, acc) =>
  Object.keys(obj).reduce((a, k) => fn(a, obj[k], k, obj), acc);
```

Aquí hay un ejemplo:

```js
transform(
  { a: 1, b: 2, c: 1 },
  (r, v, k) => {
    (r[v] || (r[v] = [])).push(k);
    return r;
  },
  {}
); // { '1': ['a', 'c'], '2': ['b'] }
```
