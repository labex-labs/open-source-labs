# Como Agrupar Elementos de um Array

Se você deseja praticar a codificação, pode começar abrindo o Terminal/SSH e digitando `node`. Quando estiver pronto, você pode agrupar os elementos de um array com base em uma função fornecida usando as seguintes etapas:

1.  Use `Array.prototype.map()` para mapear os valores do array para uma função ou nome de propriedade.
2.  Use `Array.prototype.reduce()` para criar um objeto onde as chaves são produzidas a partir dos resultados mapeados.

Aqui está um exemplo de trecho de código:

```js
const groupBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val, i) => {
      acc[val] = (acc[val] || []).concat(arr[i]);
      return acc;
    }, {});
```

Para testar o código, você pode usar os seguintes exemplos:

```js
groupBy([6.1, 4.2, 6.3], Math.floor); // {4: [4.2], 6: [6.1, 6.3]}
groupBy(["one", "two", "three"], "length"); // {3: ['one', 'two'], 5: ['three']}
```

Estes retornarão objetos com chaves baseadas na função especificada e valores que são arrays dos elementos originais que correspondem à função.
