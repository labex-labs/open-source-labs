# Gerando um Array de Inteiros Aleatórios em um Intervalo Específico

Para gerar um array de inteiros aleatórios dentro de um intervalo específico, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.from()` para criar um array vazio com o comprimento desejado.
3.  Use `Math.random()` para gerar números aleatórios e mapeá-los para o intervalo especificado. Use `Math.floor()` para convertê-los em inteiros.
4.  A função `randomIntArrayInRange()` recebe três argumentos: `min`, `max` e um argumento opcional `n` (o valor padrão é 1).
5.  Chame a função `randomIntArrayInRange()` com os valores `min`, `max` e `n` desejados para gerar o array de inteiros aleatórios.

Aqui está o código:

```js
const randomIntArrayInRange = (min, max, n = 1) =>
  Array.from(
    { length: n },
    () => Math.floor(Math.random() * (max - min + 1)) + min
  );
```

Exemplo de uso:

```js
randomIntArrayInRange(12, 35, 10); // [ 34, 14, 27, 17, 30, 27, 20, 26, 21, 14 ]
```
