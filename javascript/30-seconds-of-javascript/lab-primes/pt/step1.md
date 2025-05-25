# Gerando Primos Usando o Crivo de Eratóstenes

Para gerar números primos até um determinado número usando o Crivo de Eratóstenes, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Crie um array contendo números de `2` até o número fornecido.
3. Use `Array.prototype.filter()` para filtrar os valores que são divisíveis por qualquer número de `2` até a raiz quadrada do número fornecido.
4. Retorne o array resultante contendo os números primos.

Aqui está o código JavaScript para gerar números primos até um determinado número:

```js
const generatePrimes = (num) => {
  let arr = Array.from({ length: num - 1 }).map((x, i) => i + 2),
    sqrt = Math.floor(Math.sqrt(num)),
    numsTillSqrt = Array.from({ length: sqrt - 1 }).map((x, i) => i + 2);
  numsTillSqrt.forEach(
    (x) => (arr = arr.filter((y) => y % x !== 0 || y === x))
  );
  return arr;
};
```

Você pode chamar a função `generatePrimes()` passando o número desejado como um argumento. Por exemplo:

```js
generatePrimes(10); // [2, 3, 5, 7]
```
