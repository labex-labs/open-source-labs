# JavaScript Promises

Para verificar se um objeto é semelhante a uma Promise, use a função `isPromiseLike`. Esta função verifica se o objeto não é nulo, tem um tipo de objeto ou função, e possui uma propriedade `.then` que também é uma função.

Aqui está o código para `isPromiseLike`:

```js
const isPromiseLike = (obj) =>
  obj !== null &&
  (typeof obj === "object" || typeof obj === "function") &&
  typeof obj.then === "function";
```

Aqui estão alguns exemplos de como usar `isPromiseLike`:

```js
isPromiseLike({
  then: function () {
    return "";
  }
}); // true

isPromiseLike(null); // false

isPromiseLike({}); // false
```

Para começar a praticar a codificação em JavaScript, abra o Terminal/SSH e digite `node`.
