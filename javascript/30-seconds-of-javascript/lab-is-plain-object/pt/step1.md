# Verificar se um Valor é um Objeto Simples (Plain Object)

Para verificar se um valor é um objeto simples, siga estes passos:

- Verifique se o valor é _truthy_.
- Use `typeof` para verificar se é um objeto.
- Use `Object.prototype.constructor` para garantir que o construtor seja igual a `Object`.

Use o seguinte código para implementar essa verificação:

```js
const isPlainObject = (val) =>
  !!val && typeof val === "object" && val.constructor === Object;
```

Você pode testar esta função com os seguintes exemplos:

```js
isPlainObject({ a: 1 }); // true
isPlainObject(new Map()); // false
```

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.
