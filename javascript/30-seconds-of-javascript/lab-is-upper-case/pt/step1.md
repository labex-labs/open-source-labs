# Função para Verificar se uma String está em Maiúsculas

Para verificar se uma string está em maiúsculas, siga estes passos:

1.  Abra o Terminal/SSH.
2.  Digite `node`.
3.  Use a função `isUpperCase()` para converter a string fornecida para maiúsculas, usando `String.prototype.toUpperCase()`, e compare-a com a string original.
4.  A função retornará `true` se a string estiver em maiúsculas e `false` caso contrário.

Aqui está um exemplo de código:

```js
const isUpperCase = (str) => str === str.toUpperCase();

console.log(isUpperCase("ABC")); // true
console.log(isUpperCase("A3@$")); // true
console.log(isUpperCase("aB4")); // false
```
