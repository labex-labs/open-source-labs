# Cómo mapear un objeto a una matriz en JavaScript

Para mapear un objeto a una matriz en JavaScript, puedes utilizar la función `listify()`. Aquí te muestra cómo hacerlo:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.

2. Utiliza `Object.entries()` para obtener una matriz de pares clave-valor del objeto.

3. Utiliza `Array.prototype.reduce()` para mapear la matriz a un objeto.

4. Utiliza `mapFn` para mapear las claves y valores del objeto y `Array.prototype.push()` para agregar los valores mapeados a la matriz.

Aquí está el código de la función `listify()`:

```js
const listify = (obj, mapFn) =>
  Object.entries(obj).reduce((acc, [key, value]) => {
    acc.push(mapFn(key, value));
    return acc;
  }, []);
```

Y aquí está un ejemplo de cómo utilizarla con un objeto llamado `people`:

```js
const people = { John: { age: 42 }, Adam: { age: 39 } };
listify(people, (key, value) => ({ name: key, ...value }));
// [ { name: 'John', age: 42 }, { name: 'Adam', age: 39 } ]
```

Con esta función, puedes mapear fácilmente un objeto a una matriz en JavaScript.
