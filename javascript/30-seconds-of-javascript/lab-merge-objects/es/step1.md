# Función de fusión de objetos

Para fusionar dos o más objetos, sigue los pasos siguientes:

1. Abre la Terminal/SSH y escribe `node` para comenzar a codificar.
2. Utiliza `Array.prototype.reduce()` junto con `Object.keys()` para iterar sobre todos los objetos y claves.
3. Utiliza `Object.prototype.hasOwnProperty()` y `Array.prototype.concat()` para adjuntar valores para las claves existentes en múltiples objetos.
4. Utiliza el fragmento de código dado para crear un nuevo objeto a partir de la combinación de dos o más objetos.

```js
const merge = (...objs) =>
  [...objs].reduce(
    (acc, obj) =>
      Object.keys(obj).reduce((a, k) => {
        acc[k] = acc.hasOwnProperty(k)
          ? [].concat(acc[k]).concat(obj[k])
          : obj[k];
        return acc;
      }, {}),
    {}
  );
```

Por ejemplo, considera los siguientes objetos:

```js
const object = {
  a: [{ x: 2 }, { y: 4 }],
  b: 1
};
const other = {
  a: { z: 3 },
  b: [2, 3],
  c: "foo"
};
```

Cuando fusionas estos dos objetos utilizando la función `merge()`, obtienes el siguiente resultado:

```js
merge(object, other);
// { a: [ { x: 2 }, { y: 4 }, { z: 3 } ], b: [ 1, 2, 3 ], c: 'foo' }
```
