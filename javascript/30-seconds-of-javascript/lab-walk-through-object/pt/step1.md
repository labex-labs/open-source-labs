# Percorrendo as Chaves do Objeto (Code Walk Through Object Keys)

Para gerar uma lista de todas as chaves de um determinado objeto, use as seguintes etapas:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.

2. Defina uma função geradora chamada `walk` que recebe um objeto e um array de chaves. Use recursão para percorrer todas as chaves do objeto.

3. Dentro da função `walk`, use um loop `for...of` e `Object.keys()` para iterar sobre as chaves do objeto.

4. Use `typeof` para verificar se cada valor no objeto fornecido é, por si só, um objeto. Se o valor for um objeto, use a expressão `yield*` para delegar recursivamente à mesma função geradora, `walk`, anexando a `key` atual ao array de chaves.

5. Caso contrário, `yield` um array de chaves representando o caminho atual e o valor da `key` fornecida.

6. Use a expressão `yield*` para delegar à função geradora `walk`.

Aqui está o código:

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

Para testar o código, crie um objeto e use a função `walkThrough` para gerar uma lista de todas as suas chaves:

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
