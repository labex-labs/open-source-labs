# Como encontrar a soma de um array

Para encontrar a soma de um array de números, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a codificar.
2.  Use o método `Array.prototype.reduce()` para adicionar cada valor a um acumulador, que deve ser inicializado com o valor `0`.
3.  Aqui está o código que você pode usar para encontrar a soma do array:

```js
const sum = (...arr) => [...arr].reduce((acc, val) => acc + val, 0);
```

4.  Para testar a função `sum`, use os seguintes exemplos de código:

```js
sum(1, 2, 3, 4); // 10
sum(...[1, 2, 3, 4]); // 10
```

Seguindo estes passos, você pode facilmente encontrar a soma de um array de números usando JavaScript.
