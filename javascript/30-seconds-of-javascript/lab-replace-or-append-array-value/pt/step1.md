# Como Substituir ou Adicionar um Valor em um Array

Para substituir um item em um array ou adicioná-lo se ele não existir, siga estes passos:

1.  Use o operador spread (`...`) para criar uma cópia rasa (shallow copy) do array.
2.  Use `Array.prototype.findIndex()` para encontrar o índice do primeiro elemento que satisfaz a função de comparação fornecida `compFn`.
3.  Se nenhum elemento for encontrado, use `Array.prototype.push()` para adicionar o novo valor ao array.
4.  Caso contrário, use `Array.prototype.splice()` para substituir o valor no índice encontrado pelo novo valor.

Aqui está um exemplo de como implementar essa funcionalidade:

```js
const replaceOrAppend = (arr, val, compFn) => {
  const res = [...arr];
  const i = arr.findIndex((v) => compFn(v, val));
  if (i === -1) res.push(val);
  else res.splice(i, 1, val);
  return res;
};
```

Você pode usar esta função com um array de objetos assim:

```js
const people = [
  { name: "John", age: 30 },
  { name: "Jane", age: 28 }
];
const jane = { name: "Jane", age: 29 };
const jack = { name: "Jack", age: 28 };
replaceOrAppend(people, jane, (a, b) => a.name === b.name);
// [ { name: 'John', age: 30 }, { name: 'Jane', age: 29 } ]
replaceOrAppend(people, jack, (a, b) => a.name === b.name);
// [
//   { name: 'John', age: 30 },
//   { name: 'Jane', age: 28 },
//   { name: 'Jack', age: 28 }
// ]
```
