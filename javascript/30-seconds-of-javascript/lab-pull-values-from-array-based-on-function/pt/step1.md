# Como Remover Valores de um Array com Base em uma Função Fornecida

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

A função `pullBy` muta o array original, filtrando os valores especificados com base em uma função iteradora fornecida. Veja como funciona:

1.  Verifique se o último argumento fornecido é uma função.
2.  Use `Array.prototype.map()` para aplicar a função iteradora `fn` a todos os elementos do array.
3.  Use `Array.prototype.filter()` e `Array.prototype.includes()` para remover os valores que não são necessários.
4.  Defina `Array.prototype.length` para redefinir o comprimento do array passado para `0`.
5.  Use `Array.prototype.push()` para repovoá-lo apenas com os valores removidos.

Aqui está o código:

```js
const pullBy = (arr, ...args) => {
  const length = args.length;
  let fn = length > 1 ? args[length - 1] : undefined;
  fn = typeof fn == "function" ? (args.pop(), fn) : undefined;
  let argState = (Array.isArray(args[0]) ? args[0] : args).map((val) =>
    fn(val)
  );
  let pulled = arr.filter((v, i) => !argState.includes(fn(v)));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
};
```

E aqui está um exemplo de como usá-lo:

```js
var myArray = [{ x: 1 }, { x: 2 }, { x: 3 }, { x: 1 }];
pullBy(myArray, [{ x: 1 }, { x: 3 }], (o) => o.x); // myArray = [{ x: 2 }]
```

Observe que, neste exemplo, estamos removendo todos os elementos com uma propriedade `x` de `1` ou `3`. O `myArray` resultante conterá apenas o elemento com uma propriedade `x` de `2`.
