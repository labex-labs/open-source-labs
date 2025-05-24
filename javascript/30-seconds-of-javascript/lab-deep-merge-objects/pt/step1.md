# Como Fazer _Deep Merge_ de Objetos em JavaScript

Para fazer _deep merge_ (mesclagem profunda) de dois objetos em JavaScript, você pode usar a função `deepMerge`. Esta função recebe dois objetos e uma função como argumentos. A função é usada para lidar com chaves presentes em ambos os objetos.

Veja como a função `deepMerge` funciona:

1.  Use `Object.keys()` para obter as chaves de ambos os objetos, crie um `Set` a partir delas e use o operador spread (`...`) para criar um array de todas as chaves únicas.
2.  Use `Array.prototype.reduce()` para adicionar cada chave única ao objeto, usando `fn` para combinar os valores dos dois objetos fornecidos.

Aqui está o código para a função `deepMerge`:

```js
const deepMerge = (a, b, fn) =>
  [...new Set([...Object.keys(a), ...Object.keys(b)])].reduce(
    (acc, key) => ({ ...acc, [key]: fn(key, a[key], b[key]) }),
    {}
  );
```

Para usar a função `deepMerge`, chame-a com dois objetos e uma função. Aqui está um exemplo:

```js
deepMerge(
  { a: true, b: { c: [1, 2, 3] } },
  { a: false, b: { d: [1, 2, 3] } },
  (key, a, b) => (key === "a" ? a && b : Object.assign({}, a, b))
);
// { a: false, b: { c: [ 1, 2, 3 ], d: [ 1, 2, 3 ] } }
```

Neste exemplo, a função `deepMerge` é usada para mesclar dois objetos. O objeto resultante tem os valores de ambos os objetos mesclados.
