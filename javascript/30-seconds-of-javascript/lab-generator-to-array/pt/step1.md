# Convertendo a Saída do _Generator_ para um Array

Para converter a saída de uma função _generator_ em um array, use o operador spread (`...`). Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Aqui está um exemplo de função que converte um _generator_ em um array:

```js
const generatorToArray = (gen) => [...gen];
```

Você pode usar esta função da seguinte forma:

```js
const s = new Set([1, 2, 1, 3, 1, 4]);
generatorToArray(s.entries()); // [[ 1, 1 ], [ 2, 2 ], [ 3, 3 ], [ 4, 4 ]]
```
