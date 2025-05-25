# Encontrando a Data Máxima

Para encontrar o valor da data máxima de um array de datas fornecido, siga estes passos:

1.  Abra o Terminal ou SSH.
2.  Digite `node` para começar a praticar a codificação.
3.  Use a sintaxe de spread (espalhamento) do ES6 com `Math.max()` para encontrar o valor da data máxima.
4.  Converta o valor da data máxima em um objeto `Date` usando o construtor `Date`.

Aqui está um exemplo de trecho de código:

```js
const maxDate = (...dates) => new Date(Math.max(...dates));

const dates = [
  new Date(2017, 4, 13),
  new Date(2018, 2, 12),
  new Date(2016, 0, 10),
  new Date(2016, 0, 9)
];

maxDate(...dates); // Returns "2018-03-11T22:00:00.000Z"
```

Seguindo estes passos e usando o código fornecido, você pode facilmente encontrar o valor da data máxima de um array de datas fornecido.
