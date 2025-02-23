# Cómo fusionar profundamente objetos en JavaScript

Para fusionar profundamente dos objetos en JavaScript, puedes usar la función `deepMerge`. Esta función toma dos objetos y una función como argumentos. La función se utiliza para manejar las claves presentes en ambos objetos.

Así es como funciona la función `deepMerge`:

1. Utiliza `Object.keys()` para obtener las claves de ambos objetos, crea un `Set` a partir de ellas y utiliza el operador de propagación (`...`) para crear un array de todas las claves únicas.
2. Utiliza `Array.prototype.reduce()` para agregar cada clave única al objeto, utilizando `fn` para combinar los valores de los dos objetos dados.

Aquí está el código de la función `deepMerge`:

```js
const deepMerge = (a, b, fn) =>
  [...new Set([...Object.keys(a), ...Object.keys(b)])].reduce(
    (acc, key) => ({ ...acc, [key]: fn(key, a[key], b[key]) }),
    {}
  );
```

Para usar la función `deepMerge`, llámala con dos objetos y una función. Aquí hay un ejemplo:

```js
deepMerge(
  { a: true, b: { c: [1, 2, 3] } },
  { a: false, b: { d: [1, 2, 3] } },
  (key, a, b) => (key === "a" ? a && b : Object.assign({}, a, b))
);
// { a: false, b: { c: [ 1, 2, 3 ], d: [ 1, 2, 3 ] } }
```

En este ejemplo, la función `deepMerge` se utiliza para fusionar dos objetos. El objeto resultante tiene los valores de ambos objetos fusionados juntos.
