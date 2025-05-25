# Algoritmo de Embaralhamento de Array

Para embaralhar um array em JavaScript, use o algoritmo de Fisher-Yates. Este algoritmo reordena os elementos do array aleatoriamente e retorna um novo array.

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Aqui está o código para o algoritmo de Fisher-Yates:

```js
const shuffle = ([...arr]) => {
  let m = arr.length;
  while (m) {
    const i = Math.floor(Math.random() * m--);
    [arr[m], arr[i]] = [arr[i], arr[m]];
  }
  return arr;
};
```

Para embaralhar um array, passe o array para a função `shuffle` e ela retornará o array embaralhado. Por exemplo:

```js
const foo = [1, 2, 3];
shuffle(foo); // returns [2, 3, 1], and foo is still [1, 2, 3]
```
