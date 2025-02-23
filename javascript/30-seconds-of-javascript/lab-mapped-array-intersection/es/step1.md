# Instrucciones para encontrar la intersección de arrays mapeados

Para encontrar los elementos comunes en dos arrays después de aplicar una función a cada elemento de ambos arrays, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node`.
2. Utilice el código proporcionado a continuación:

```js
const intersectionBy = (a, b, fn) => {
  const s = new Set(b.map(fn));
  return [...new Set(a)].filter((x) => s.has(fn(x)));
};
```

3. En el código, reemplace `a` y `b` con sus arrays y `fn` con la función que desea aplicar a cada elemento.
4. Ejecute el código para obtener el array resultante con los elementos comunes.

Ejemplo:

```js
intersectionBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [2.1]
intersectionBy(
  [{ title: "Apple" }, { title: "Orange" }],
  [{ title: "Orange" }, { title: "Melon" }],
  (x) => x.title
); // [{ title: 'Orange' }]
```

En el primer ejemplo, la función `Math.floor` se aplica a los arrays `[2.1, 1.2]` y `[2.3, 3.4]`, devolviendo el elemento común `[2.1]`.
En el segundo ejemplo, la función `x => x.title` se aplica a los arrays `[{ title: 'Apple' }, { title: 'Orange' }]` y `[{ title: 'Orange' }, { title: 'Melon' }]`, devolviendo el elemento común `[{ title: 'Orange' }]`.
