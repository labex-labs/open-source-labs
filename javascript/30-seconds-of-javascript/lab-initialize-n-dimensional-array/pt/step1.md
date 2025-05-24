# Como Inicializar um Array N-Dimensional em JavaScript

Para criar um array N-dimensional em JavaScript, você pode usar a função `initializeNDArray`. Esta função recebe um valor e qualquer número de dimensões como argumentos e retorna um novo array inicializado com esse valor.

Para usar `initializeNDArray`, você pode seguir estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a codificar.
2.  Use recursão para criar o array com o número de dimensões fornecido.
3.  Use `Array.from()` e `Array.prototype.map()` para gerar linhas, onde cada linha é um novo array inicializado usando `initializeNDArray()`.

Aqui está o código para a função `initializeNDArray`:

```js
const initializeNDArray = (val, ...args) =>
  args.length === 0
    ? val
    : Array.from({ length: args[0] }).map(() =>
        initializeNDArray(val, ...args.slice(1))
      );
```

Você pode então chamar `initializeNDArray` com o valor desejado e o número de dimensões. Por exemplo:

```js
initializeNDArray(1, 3); // [1, 1, 1]
initializeNDArray(5, 2, 2, 2); // [[[5, 5], [5, 5]], [[5, 5], [5, 5]]]
```
