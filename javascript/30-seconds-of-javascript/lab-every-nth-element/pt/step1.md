# Função para Retornar Cada N-ésimo Elemento de um Array

Para retornar cada `nth` elemento em um array, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `Array.prototype.filter()` para criar um novo array que contenha cada `nth` elemento de um array dado.
3.  Use a seguinte função para implementar o passo acima:

```js
const everyNth = (arr, nth) => arr.filter((e, i) => i % nth === nth - 1);
```

4.  Para testar a função, use o seguinte código:

```js
everyNth([1, 2, 3, 4, 5, 6], 2); // [ 2, 4, 6 ]
```

Isso retornará um novo array com cada segundo elemento do array de entrada.
