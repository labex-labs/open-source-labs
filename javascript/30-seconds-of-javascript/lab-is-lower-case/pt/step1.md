# Função JavaScript para Verificar se uma String está em Minúsculas

Para verificar se uma determinada string está em minúsculas, você pode usar a seguinte função JavaScript. Primeiro, converta a string para minúsculas usando `String.prototype.toLowerCase()` e, em seguida, compare-a com a string original usando igualdade estrita (`===`).

```js
const isLowerCase = (str) => str === str.toLowerCase();
```

Aqui está um exemplo de uso:

```js
isLowerCase("abc"); // true
isLowerCase("a3@$"); // true
isLowerCase("Ab4"); // false
```

Para usar esta função, abra o Terminal/SSH e digite `node`.
