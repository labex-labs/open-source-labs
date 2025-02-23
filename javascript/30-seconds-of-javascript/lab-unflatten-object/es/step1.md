# Cómo desaplanar un objeto en JavaScript

Para desaplanar un objeto con rutas para las claves en JavaScript, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.

2. Utiliza `Array.prototype.reduce()` anidado para convertir la ruta plana en un nodo hoja.

3. Utiliza `String.prototype.split()` para dividir cada clave con un delimitador de puntos y `Array.prototype.reduce()` para agregar objetos en función de las claves.

4. Si el acumulador actual ya contiene un valor para una clave en particular, devuelve su valor como el siguiente acumulador.

5. De lo contrario, agrega el par clave-valor adecuado al objeto acumulador y devuelve el valor como el acumulador.

Aquí está el código para la función `unflattenObject`:

```js
const unflattenObject = (obj) =>
  Object.keys(obj).reduce((res, k) => {
    k.split(".").reduce(
      (acc, e, i, keys) =>
        acc[e] ||
        (acc[e] = isNaN(Number(keys[i + 1]))
          ? keys.length - 1 === i
            ? obj[k]
            : {}
          : []),
      res
    );
    return res;
  }, {});
```

Puedes utilizar la función `unflattenObject` para desaplanar un objeto en JavaScript:

```js
unflattenObject({ "a.b.c": 1, d: 1 }); // { a: { b: { c: 1 } }, d: 1 }
unflattenObject({ "a.b": 1, "a.c": 2, d: 3 }); // { a: { b: 1, c: 2 }, d: 3 }
unflattenObject({ "a.b.0": 8, d: 3 }); // { a: { b: [ 8 ] }, d: 3 }
```
