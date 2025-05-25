# Como Particionar um Array em Dois com Base em uma Função

Para particionar um array em dois com base em uma função fornecida, siga estas etapas:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.reduce()` para criar um array de dois arrays.
3.  Use `Array.prototype.push()` para adicionar elementos para os quais `fn` retorna `true` ao primeiro array e elementos para os quais `fn` retorna `false` ao segundo.

Aqui está o código que você pode usar:

```js
const partition = (arr, fn) =>
  arr.reduce(
    (acc, val, i, arr) => {
      acc[fn(val, i, arr) ? 0 : 1].push(val);
      return acc;
    },
    [[], []]
  );
```

Para testar este código, você pode usar o seguinte exemplo:

```js
const users = [
  { user: "barney", age: 36, active: false },
  { user: "fred", age: 40, active: true }
];
partition(users, (o) => o.active);
// [
//   [{ user: 'fred', age: 40, active: true }],
//   [{ user: 'barney', age: 36, active: false }]
// ]
```

Isso retornará um array de dois arrays, onde o primeiro array contém todos os elementos para os quais a função fornecida retorna `true`, e o segundo array contém todos os elementos para os quais a função fornecida retorna `false`.
