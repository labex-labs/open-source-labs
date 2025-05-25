# Função para Verificar se o Valor é do Tipo

Para verificar se um valor fornecido é de um tipo especificado, siga estes passos:

- Certifique-se de que o valor não é `undefined` ou `null` usando `Array.prototype.includes()`.
- Use `Object.prototype.constructor` para comparar a propriedade construtora (constructor property) no valor com o `type` especificado.
- A função `is()` abaixo realiza essas verificações e retorna `true` se o valor for do tipo especificado e `false` caso contrário.

```js
const is = (type, val) => ![, null].includes(val) && val.constructor === type;
```

Você pode usar `is()` para verificar se um valor é de vários tipos, como `Array`, `ArrayBuffer`, `Map`, `RegExp`, `Set`, `WeakMap`, `WeakSet`, `String`, `Number` e `Boolean`. Por exemplo:

```js
is(Array, [1]); // true
is(Map, new Map()); // true
is(String, ""); // true
is(Number, 1); // true
is(Boolean, true); // true
```
