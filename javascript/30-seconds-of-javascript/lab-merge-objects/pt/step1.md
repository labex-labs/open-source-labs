# Função de Mesclagem de Objetos

Para mesclar dois ou mais objetos, siga os passos fornecidos:

1.  Abra o Terminal/SSH e digite `node` para começar a codificar.
2.  Use `Array.prototype.reduce()` juntamente com `Object.keys()` para iterar sobre todos os objetos e chaves.
3.  Use `Object.prototype.hasOwnProperty()` e `Array.prototype.concat()` para anexar valores para chaves existentes em múltiplos objetos.
4.  Use o trecho de código fornecido para criar um novo objeto a partir da combinação de dois ou mais objetos.

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

Por exemplo, considere os seguintes objetos:

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

Quando você mescla esses dois objetos usando a função `merge()`, você obtém o seguinte resultado:

```js
merge(object, other);
// { a: [ { x: 2 }, { y: 4 }, { z: 3 } ], b: [ 1, 2, 3 ], c: 'foo' }
```
