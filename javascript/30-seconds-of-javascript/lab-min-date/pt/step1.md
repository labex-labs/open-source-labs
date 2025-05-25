# Como Encontrar a Data Mínima em JavaScript

Para encontrar o valor da data mínima em JavaScript, você pode usar a sintaxe spread do ES6 com `Math.min()` e o construtor `Date`. Aqui está um trecho de código de exemplo:

```js
const minDate = (...dates) => new Date(Math.min(...dates));
```

Para usar esta função, crie um array de objetos `Date` e passe-o para `minDate()` usando a sintaxe spread. Aqui está um exemplo:

```js
const dates = [
  new Date(2017, 4, 13),
  new Date(2018, 2, 12),
  new Date(2016, 0, 10),
  new Date(2016, 0, 9)
];
minDate(...dates); // Retorna um objeto `Date` representando 2016-01-08T22:00:00.000Z
```

Ao usar este código, você pode facilmente encontrar o valor da data mínima em JavaScript.
