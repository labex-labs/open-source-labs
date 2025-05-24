# Verificar se um Valor é Semelhante a um Array

Para verificar se um valor é semelhante a um array, siga estes passos:

1. Abra o Terminal/SSH.
2. Digite `node`.
3. Use o seguinte código para verificar se o argumento fornecido é iterável:

```js
const isArrayLike = (obj) =>
  obj != null && typeof obj[Symbol.iterator] === "function";
```

4. A função retornará `true` se o argumento fornecido for um objeto semelhante a um array e `false` caso contrário.
5. Por exemplo:

```js
isArrayLike([1, 2, 3]); // true
isArrayLike(document.querySelectorAll(".className")); // true
isArrayLike("abc"); // true
isArrayLike(null); // false
```
