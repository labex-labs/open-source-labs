# Verificando a Igualdade dos Elementos de um Array

Para verificar se todos os elementos em um array são iguais, você pode usar o método `Array.prototype.every()`, que compara todos os elementos com o primeiro.

Veja como você pode implementá-lo:

```js
const allEqual = (arr) => arr.every((val) => val === arr[0]);
```

Observe que o operador de `comparação estrita` (strict comparison) é usado para comparar os elementos. Este operador não considera a auto-inequação de `NaN`.

Exemplo de uso:

```js
allEqual([1, 2, 3, 4, 5, 6]); // false
allEqual([1, 1, 1, 1]); // true
```
