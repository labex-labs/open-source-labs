# Como Encontrar o Mínimo e o Máximo de um Array Usando uma Função Fornecida

Para praticar a codificação, abra o Terminal ou SSH e digite `node`.

Aqui está uma função que retorna os valores mínimo e máximo de um array, com base em uma função fornecida que define a regra de comparação:

```js
const reduceWhich = (arr, comparator = (a, b) => a - b) =>
  arr.reduce((a, b) => (comparator(a, b) >= 0 ? b : a));
```

Para usá-la, siga estes passos:

1.  Chame `reduceWhich` com o array que você deseja processar e a função `comparator` opcional.
2.  A função `reduceWhich` usará `Array.prototype.reduce()` em combinação com a função `comparator` para retornar o elemento apropriado no array.
3.  Se você omitir o segundo argumento (`comparator`), a função padrão será usada, que retorna o elemento mínimo no array.

Aqui estão alguns exemplos de como usar `reduceWhich`:

```js
reduceWhich([1, 3, 2]); // 1
reduceWhich([1, 3, 2], (a, b) => b - a); // 3
reduceWhich(
  [
    { name: "Tom", age: 12 },
    { name: "Jack", age: 18 },
    { name: "Lucy", age: 9 }
  ],
  (a, b) => a.age - b.age
); // {name: 'Lucy', age: 9}
```

Nos exemplos acima, a primeira chamada para `reduceWhich` retorna o valor mínimo do array `[1, 3, 2]`, que é `1`. A segunda chamada retorna o valor máximo do mesmo array, com base na função `comparator` que inverte a ordem de comparação. A terceira chamada retorna o objeto no array que possui a propriedade `age` mínima, com base na função `comparator` que compara as propriedades `age` dos objetos.
