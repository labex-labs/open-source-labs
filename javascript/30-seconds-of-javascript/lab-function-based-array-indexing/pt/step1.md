# Função para Indexar um Array

Para indexar um array usando uma função, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use `Array.prototype.reduce()` para criar um objeto a partir do array.
3. Aplique a função fornecida a cada valor do array para produzir uma chave e adicione o par chave-valor ao objeto.

Aqui está um exemplo de trecho de código:

```js
const indexBy = (arr, fn) =>
  arr.reduce((obj, v, i) => {
    obj[fn(v, i, arr)] = v;
    return obj;
  }, {});
```

Você pode usar esta função da seguinte forma:

```js
indexBy(
  [
    { id: 10, name: "apple" },
    { id: 20, name: "orange" }
  ],
  (x) => x.id
);
// { '10': { id: 10, name: 'apple' }, '20': { id: 20, name: 'orange' } }
```

Esta função cria um objeto a partir de um array, mapeando cada valor para uma chave usando uma função fornecida. O objeto resultante contém pares chave-valor, onde as chaves são produzidas pela função e os valores são os elementos originais do array.
