# Función para invertir un objeto

Para invertir los pares clave-valor de un objeto sin alterar el objeto original, utiliza la función `invertKeyValues`.

- Llama a la función escribiendo `invertKeyValues(obj, fn)` en la Terminal/SSH, donde `obj` es el objeto que se va a invertir y `fn` es una función opcional que se aplicará a la clave invertida.

- Los métodos `Object.keys()` y `Array.prototype.reduce()` se utilizan para crear un nuevo objeto con pares clave-valor invertidos, y si se proporciona una función, se aplica a cada clave invertida.

- Si se omite `fn`, la función devuelve solo las claves invertidas sin ninguna función aplicada a ellas.

- La función devuelve un objeto en el que cada valor invertido es una matriz de claves responsables de generar el valor invertido.

```js
const invertKeyValues = (obj, fn) =>
  Object.keys(obj).reduce((acc, key) => {
    const val = fn ? fn(obj[key]) : obj[key];
    acc[val] = acc[val] || [];
    acc[val].push(key);
    return acc;
  }, {});
```

Uso de ejemplo:

```js
invertKeyValues({ a: 1, b: 2, c: 1 }); // { 1: [ 'a', 'c' ], 2: [ 'b' ] }
invertKeyValues({ a: 1, b: 2, c: 1 }, (value) => "group" + value);
// { group1: [ 'a', 'c' ], group2: [ 'b' ] }
```
