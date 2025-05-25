# Como Juntar um Array em uma String

Para juntar todos os elementos de um array em uma string, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use a função `join()` com os seguintes parâmetros:
    - `arr`: o array a ser juntado.
    - `separator` (opcional): o separador a ser usado entre os elementos do array. Se não for especificado, o separador padrão `,` será usado.
    - `end` (opcional): o separador a ser usado entre os dois últimos elementos do array. Se não for especificado, o mesmo valor de `separator` será usado por padrão.
3.  A função `join()` usa `Array.prototype.reduce()` para combinar os elementos do array em uma string.
4.  A string final é retornada.

Aqui está o código para a função `join()`:

```js
const join = (arr, separator = ",", end = separator) =>
  arr.reduce(
    (acc, val, i) =>
      i === arr.length - 2
        ? acc + val + end
        : i === arr.length - 1
          ? acc + val
          : acc + val + separator,
    ""
  );
```

E aqui estão alguns exemplos de como usar a função `join()`:

```js
join(["pen", "pineapple", "apple", "pen"], ",", "&"); // 'pen,pineapple,apple&pen'
join(["pen", "pineapple", "apple", "pen"], ","); // 'pen,pineapple,apple,pen'
join(["pen", "pineapple", "apple", "pen"]); // 'pen,pineapple,apple,pen'
```
