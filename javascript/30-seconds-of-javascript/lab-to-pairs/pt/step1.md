# Convertendo um Objeto em Pares

Para converter um objeto em um array de pares chave-valor, use a função `toPairs`. Para começar a codificar, abra o Terminal/SSH e digite `node`.

A função `toPairs` funciona da seguinte maneira:

- Primeiro, verifica se `Symbol.iterator` está definido para o objeto iterável fornecido.
- Se `Symbol.iterator` estiver definido, ele usa `Array.prototype.entries()` para obter um iterador para o objeto e, em seguida, converte o resultado em um array de arrays de pares chave-valor usando `Array.from()`.
- Se `Symbol.iterator` não estiver definido para o objeto, ele usa `Object.entries()` em vez disso.

Aqui está o código para a função `toPairs`:

```js
const toPairs = (obj) =>
  obj[Symbol.iterator] instanceof Function && obj.entries instanceof Function
    ? Array.from(obj.entries())
    : Object.entries(obj);
```

Você pode usar a função `toPairs` com vários tipos de objetos, como:

```js
toPairs({ a: 1, b: 2 }); // [['a', 1], ['b', 2]]
toPairs([2, 4, 8]); // [[0, 2], [1, 4], [2, 8]]
toPairs("shy"); // [['0', 's'], ['1', 'h'], ['2', 'y']]
toPairs(new Set(["a", "b", "c", "a"])); // [['a', 'a'], ['b', 'b'], ['c', 'c']]
```
