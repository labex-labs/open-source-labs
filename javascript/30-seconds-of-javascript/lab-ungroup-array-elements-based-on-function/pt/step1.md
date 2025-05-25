# Como Desagrupar Elementos de Array com Base em uma Função

Se você precisar desagrupar elementos em um array produzido por `zip` e aplicar uma função, pode usar `unzipWith`. Veja como você pode implementá-lo:

1. Use `Math.max()` e o operador spread (`...`) para obter o subarray mais longo no array e `Array.prototype.map()` para transformar cada elemento em um array.
2. Use `Array.prototype.reduce()` e `Array.prototype.forEach()` para mapear valores agrupados em arrays individuais.
3. Use `Array.prototype.map()` e o operador spread (`...`) para aplicar `fn` a cada grupo individual de elementos.

```js
const unzipWith = (arr, fn) =>
  arr
    .reduce(
      (acc, val) => (val.forEach((v, i) => acc[i].push(v)), acc),
      Array.from({
        length: Math.max(...arr.map((x) => x.length))
      }).map((x) => [])
    )
    .map((val) => fn(...val));
```

Para usar `unzipWith`, abra o Terminal/SSH e digite `node`. Em seguida, você pode executar o seguinte exemplo:

```js
unzipWith(
  [
    [1, 10, 100],
    [2, 20, 200]
  ],
  (...args) => args.reduce((acc, v) => acc + v, 0)
);
// [3, 30, 300]
```

Isso criará um array de elementos desagrupando os elementos no array de entrada produzido por `zip` e aplicando a função fornecida.
