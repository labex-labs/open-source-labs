# Encontrando o N-ÉSIMO Elemento de um Array

Para encontrar o n-ésimo elemento de um array, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use `Array.prototype.slice()` para criar um novo array contendo o n-ésimo elemento.
3. Se o índice estiver fora dos limites (out of bounds), retorne `undefined`.
4. Omita o segundo argumento, `n`, para obter o primeiro elemento do array.

Aqui está um exemplo de código que implementa isso:

```js
const nthElement = (arr, n = 0) =>
  (n === -1 ? arr.slice(n) : arr.slice(n, n + 1))[0];
```

Você pode testar esta função com os seguintes exemplos:

```js
nthElement(["a", "b", "c"], 1); // Output: 'b'
nthElement(["a", "b", "b"], -3); // Output: 'a'
```

Seguindo estes passos, você pode facilmente encontrar o n-ésimo elemento de um array usando JavaScript.
