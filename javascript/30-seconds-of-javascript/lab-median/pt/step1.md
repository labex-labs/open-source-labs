# Como Calcular a Mediana de um Array de Números

Para calcular a mediana de um array de números, siga estes passos:

1.  Encontre o meio do array.
2.  Use `Array.prototype.sort()` para ordenar os valores.
3.  Se `Array.prototype.length` for ímpar, retorne o número no ponto médio. Se for par, retorne a média dos dois números do meio.
4.  Para começar a praticar a codificação e usar `node`, abra o Terminal/SSH e digite `node`.

Aqui está um exemplo de trecho de código que implementa essa lógica:

```js
const median = (arr) => {
  const mid = Math.floor(arr.length / 2),
    nums = [...arr].sort((a, b) => a - b);
  return arr.length % 2 !== 0 ? nums[mid] : (nums[mid - 1] + nums[mid]) / 2;
};
```

Você pode chamar esta função com um array de números, como mostrado abaixo:

```js
median([5, 6, 50, 1, -5]); // 5
```
