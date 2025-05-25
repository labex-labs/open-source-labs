# Como Ordenar um Array de Objetos com Base na Ordem de uma Propriedade

Para ordenar um array de objetos com base na ordem de uma propriedade, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.reduce()` para criar um objeto a partir do array `order`, com os valores como chaves e seus índices originais como valor.
3.  Use `Array.prototype.sort()` para ordenar o array fornecido, ignorando elementos para os quais `prop` está vazio ou não está no array `order`.

Aqui está um trecho de código de exemplo para ordenar um array de objetos com base na ordem de uma propriedade:

```js
const orderWith = (arr, prop, order) => {
  const orderValues = order.reduce((acc, v, i) => {
    acc[v] = i;
    return acc;
  }, {});
  return [...arr].sort((a, b) => {
    if (orderValues[a[prop]] === undefined) return 1;
    if (orderValues[b[prop]] === undefined) return -1;
    return orderValues[a[prop]] - orderValues[b[prop]];
  });
};
```

Você pode usar a função `orderWith` para ordenar um array de objetos com base na ordem de uma propriedade. Por exemplo:

```js
const users = [
  { name: "fred", language: "Javascript" },
  { name: "barney", language: "TypeScript" },
  { name: "frannie", language: "Javascript" },
  { name: "anna", language: "Java" },
  { name: "jimmy" },
  { name: "nicky", language: "Python" }
];
orderWith(users, "language", ["Javascript", "TypeScript", "Java"]);
/*
[
  { name: 'fred', language: 'Javascript' },
  { name: 'frannie', language: 'Javascript' },
  { name: 'barney', language: 'TypeScript' },
  { name: 'anna', language: 'Java' },
  { name: 'jimmy' },
  { name: 'nicky', language: 'Python' }
]
*/
```
