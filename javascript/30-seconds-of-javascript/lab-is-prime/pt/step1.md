# Função para verificar se um número é primo

Para praticar a codificação, abra o Terminal/SSH e digite `node`. Esta função verifica se um inteiro dado é um número primo. Aqui estão os passos para verificar se um número é primo:

1. Verifique os números de `2` até a raiz quadrada do número dado.
2. Se algum deles dividir o número dado, retorne `false`.
3. Se nenhum deles dividir o número dado, retorne `true`, a menos que o número seja menor que `2`.

Aqui está o código para implementar esta função em JavaScript:

```js
const isPrime = (num) => {
  const boundary = Math.floor(Math.sqrt(num));
  for (let i = 2; i <= boundary; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return num >= 2;
};
```

Você pode testar a função chamando-a com um número como argumento:

```js
isPrime(11); // true
```
