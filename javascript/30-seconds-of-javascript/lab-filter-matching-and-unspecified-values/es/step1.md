# Filtrado de objetos por condición y claves

Para filtrar una matriz de objetos basada en una condición, mientras también se filtran las claves no especificadas, use la función `reducedFilter()`.

A continuación, se presentan los pasos a seguir:

1. Utilice `Array.prototype.filter()` para filtrar la matriz según el predicado `fn` de modo que devuelva los objetos para los cuales la condición devolvió un valor verdadero.

2. Utilice `Array.prototype.map()` en la matriz filtrada para devolver el nuevo objeto.

3. Utilice `Array.prototype.reduce()` para filtrar las claves que no se suministraron como argumento `keys`.

```js
const reducedFilter = (data, keys, fn) =>
  data.filter(fn).map((el) =>
    keys.reduce((acc, key) => {
      acc[key] = el[key];
      return acc;
    }, {})
  );
```

A continuación, se muestra un ejemplo de uso de la función `reducedFilter()`:

```js
const data = [
  {
    id: 1,
    name: "john",
    age: 24
  },
  {
    id: 2,
    name: "mike",
    age: 50
  }
];

reducedFilter(data, ["id", "name"], (item) => item.age > 24);
// Output: [{ id: 2, name:'mike'}]
```

Para comenzar a practicar la codificación, abra la Terminal/SSH y escriba `node`.
