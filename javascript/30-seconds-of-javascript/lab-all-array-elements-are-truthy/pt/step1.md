# Verificando se Todos os Elementos de um Array São Verdadeiros

Para verificar se todos os elementos em uma coleção são `true`, você pode usar o método `Array.prototype.every()`. Este método recebe uma função predicado como argumento e retorna `true` se a função for avaliada como `true` para todos os elementos no array.

Para simplificar o código, você pode usar uma função chamada `all` que recebe um array e uma função predicado opcional como argumentos. A função usa `Array.prototype.every()` para verificar se todos os elementos no array retornam `true` com base na função fornecida. Se nenhuma função for fornecida, `Boolean` é usado como padrão.

Aqui está um exemplo de como usar a função `all`:

```js
const all = (arr, fn = Boolean) => arr.every(fn);

all([4, 2, 3], (x) => x > 1); // true
all([1, 2, 3]); // true
```
