# Recorrido del código por las claves de un objeto

Para generar una lista de todas las claves de un objeto dado, siga los siguientes pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.

2. Defina una función generadora llamada `walk` que tome un objeto y una matriz de claves. Utilice la recursividad para recorrer todas las claves del objeto.

3. Dentro de la función `walk`, utilice un bucle `for...of` y `Object.keys()` para iterar sobre las claves del objeto.

4. Utilice `typeof` para comprobar si cada valor en el objeto dado es a su vez un objeto. Si el valor es un objeto, utilice la expresión `yield*` para delegar recursivamente a la misma función generadora, `walk`, agregando la `key` actual a la matriz de claves.

5. De lo contrario, `yield` una matriz de claves que representen el camino actual y el valor de la `key` dada.

6. Utilice la expresión `yield*` para delegar a la función generadora `walk`.

Aquí está el código:

```js
const walkThrough = function* (obj) {
  const walk = function* (x, previous = []) {
    for (let key of Object.keys(x)) {
      if (typeof x[key] === "object") yield* walk(x[key], [...previous, key]);
      else yield [[...previous, key], x[key]];
    }
  };
  yield* walk(obj);
};
```

Para probar el código, cree un objeto y utilice la función `walkThrough` para generar una lista de todas sus claves:

```js
const obj = {
  a: 10,
  b: 20,
  c: {
    d: 10,
    e: 20,
    f: [30, 40]
  },
  g: [
    {
      h: 10,
      i: 20
    },
    {
      j: 30
    },
    40
  ]
};
[...walkThrough(obj)];
/*
[
  [['a'], 10],
  [['b'], 20],
  [['c', 'd'], 10],
  [['c', 'e'], 20],
  [['c', 'f', '0'], 30],
  [['c', 'f', '1'], 40],
  [['g', '0', 'h'], 10],
  [['g', '0', 'i'], 20],
  [['g', '1', 'j'], 30],
  [['g', '2'], 40]
]
*/
```
