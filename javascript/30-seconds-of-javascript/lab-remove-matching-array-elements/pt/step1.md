# Removendo Elementos Correspondentes de um Array

Para remover elementos específicos de um array com base em uma condição dada, você pode usar a função `remove`. Esta função muta o array original removendo elementos para os quais a função fornecida retorna `false`.

Aqui estão os passos para usar a função `remove`:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use `Array.prototype.filter()` para encontrar elementos do array que retornam valores truthy.
3. Use `Array.prototype.reduce()` para remover elementos usando `Array.prototype.splice()`.
4. A função de callback é invocada com três argumentos (valor, índice, array).

```js
const remove = (arr, func) =>
  Array.isArray(arr)
    ? arr.filter(func).reduce((acc, val) => {
        arr.splice(arr.indexOf(val), 1);
        return acc.concat(val);
      }, [])
    : [];
```

Aqui está um exemplo de como usar a função `remove`:

```js
remove([1, 2, 3, 4], (n) => n % 2 === 0); // [2, 4]
```

Isso retornará um novo array com os elementos removidos.
