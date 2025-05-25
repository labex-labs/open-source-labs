# Array de Valores Sucessivos

Para criar um array de valores sucessivos em JavaScript, você pode usar o método `Array.prototype.reduce()`. Este método aplica uma função a um acumulador e a cada elemento do array, da esquerda para a direita, e retorna um array dos valores sucessivamente reduzidos.

Veja como usar a função `reduceSuccessive` para aplicar a função fornecida ao array fornecido, armazenando cada novo resultado:

```js
const reduceSuccessive = (arr, fn, acc) =>
  arr.reduce(
    (res, val, i, arr) => (res.push(fn(res.slice(-1)[0], val, i, arr)), res),
    [acc]
  );
```

Você pode então chamar a função `reduceSuccessive` com um array, uma função e um valor inicial para o acumulador:

```js
reduceSuccessive([1, 2, 3, 4, 5, 6], (acc, val) => acc + val, 0);
// [0, 1, 3, 6, 10, 15, 21]
```

Para começar a praticar a codificação com esta função, abra o Terminal/SSH e digite `node`.
