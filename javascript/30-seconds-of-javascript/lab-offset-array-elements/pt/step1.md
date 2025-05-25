# Como Deslocar Elementos de Array em JavaScript

Para mover um número especificado de elementos para o final de um array JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `Array.prototype.slice()` duas vezes para obter os elementos após o índice especificado e os elementos antes dele.
3.  Use o operador spread (`...`) para combinar os dois arrays em um só.
4.  Se o `offset` for negativo, os elementos serão movidos do final para o início do array.

Aqui está um trecho de código de exemplo que implementa a função `offset`:

```js
const offset = (arr, offset) => [...arr.slice(offset), ...arr.slice(0, offset)];
```

Você pode então chamar a função com seu array desejado e valores de offset:

```js
offset([1, 2, 3, 4, 5], 2); // [3, 4, 5, 1, 2]
offset([1, 2, 3, 4, 5], -2); // [4, 5, 1, 2, 3]
```
