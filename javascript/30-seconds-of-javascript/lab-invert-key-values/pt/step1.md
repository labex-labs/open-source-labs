# Função para Inverter um Objeto

Para inverter os pares chave-valor de um objeto sem alterar o objeto original, use a função `invertKeyValues`.

- Chame a função digitando `invertKeyValues(obj, fn)` no Terminal/SSH, onde `obj` é o objeto a ser invertido e `fn` é uma função opcional a ser aplicada à chave invertida.

- Os métodos `Object.keys()` e `Array.prototype.reduce()` são usados para criar um novo objeto com pares chave-valor invertidos e, se uma função for fornecida, ela é aplicada a cada chave invertida.

- Se `fn` for omitida, a função retorna apenas as chaves invertidas sem qualquer função aplicada a elas.

- A função retorna um objeto com cada valor invertido sendo um array de chaves responsáveis por gerar o valor invertido.

```js
const invertKeyValues = (obj, fn) =>
  Object.keys(obj).reduce((acc, key) => {
    const val = fn ? fn(obj[key]) : obj[key];
    acc[val] = acc[val] || [];
    acc[val].push(key);
    return acc;
  }, {});
```

Exemplo de uso:

```js
invertKeyValues({ a: 1, b: 2, c: 1 }); // { 1: [ 'a', 'c' ], 2: [ 'b' ] }
invertKeyValues({ a: 1, b: 2, c: 1 }, (value) => "group" + value);
// { group1: [ 'a', 'c' ], group2: [ 'b' ] }
```
