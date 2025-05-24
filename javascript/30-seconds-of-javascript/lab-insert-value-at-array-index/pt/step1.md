# Como Inserir um Valor em um Índice Específico em um Array usando JavaScript

Para inserir um valor em um índice específico em um array usando JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `Array.prototype.splice()` com um índice apropriado e uma contagem de exclusão (delete count) de `0`, espalhando os valores fornecidos para serem inseridos.
3.  A função `insertAt` recebe um array, um índice e um ou mais valores a serem inseridos após o índice especificado.
4.  A função muta o array original e retorna o array modificado.

Aqui está um exemplo da função `insertAt` em ação:

```js
const insertAt = (arr, i, ...v) => {
  arr.splice(i + 1, 0, ...v);
  return arr;
};

let myArray = [1, 2, 3, 4];
insertAt(myArray, 2, 5); // myArray = [1, 2, 3, 5, 4]

let otherArray = [2, 10];
insertAt(otherArray, 0, 4, 6, 8); // otherArray = [2, 4, 6, 8, 10]
```

No exemplo acima, a função `insertAt` é usada para inserir o valor `5` após o segundo índice do array `myArray`, e para inserir os valores `4`, `6` e `8` após o primeiro índice do array `otherArray`.
