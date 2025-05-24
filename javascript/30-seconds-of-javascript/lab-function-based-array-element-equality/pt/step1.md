# Verificando se os Elementos de um Array São Iguais com uma Função Dada

Para verificar se todos os elementos em um array são iguais, use a função `allEqualBy`. Esta função aplica uma função de mapeamento (mapping function) dada, `fn`, ao primeiro elemento do array `arr`. Em seguida, verifica se `fn` retorna o mesmo valor para todos os elementos no array que retornou para o primeiro elemento, usando `Array.prototype.every()`. A função utiliza o operador de comparação estrita, que não considera a auto-desigualdade de `NaN`.

Aqui está o código para `allEqualBy`:

```js
const allEqualBy = (arr, fn) => {
  const eql = fn(arr[0]);
  return arr.every((val) => fn(val) === eql);
};
```

Você pode usar `allEqualBy` desta forma:

```js
allEqualBy([1.1, 1.2, 1.3], Math.round); // true
allEqualBy([1.1, 1.3, 1.6], Math.round); // false
```

Para começar a praticar a codificação com esta função, abra o Terminal/SSH e digite `node`.
