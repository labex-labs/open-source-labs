# Validar Chaves de Objeto

Para garantir que todas as chaves em um objeto correspondam às `keys` especificadas, siga estes passos:

- Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
- Use `Object.keys()` para recuperar as chaves do objeto, `obj`.
- Use `Array.prototype.every()` e `Array.prototype.includes()` para validar que cada chave no objeto está incluída no array `keys`.

Aqui está um exemplo de implementação:

```js
const validateObjectKeys = (obj, keys) =>
  Object.keys(obj).every((key) => keys.includes(key));
```

Você pode usar a função desta forma:

```js
validateObjectKeys({ id: 10, name: "apple" }, ["id", "name"]); // true
validateObjectKeys({ id: 10, name: "apple" }, ["id", "type"]); // false
```
