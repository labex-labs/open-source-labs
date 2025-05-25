# Remover Chaves de um Objeto

Para remover chaves específicas de um objeto, use a função `omit`, que recebe um objeto e um array de chaves a serem removidas.

- O método `Object.keys()` é usado para obter todas as chaves do objeto.
- O método `Array.prototype.filter()` é então usado para remover as chaves especificadas da lista de chaves.
- Finalmente, `Array.prototype.reduce()` é usado para criar um novo objeto com os pares chave-valor restantes.

```js
const omit = (obj, keysToRemove) =>
  Object.keys(obj)
    .filter((key) => !keysToRemove.includes(key))
    .reduce((newObj, key) => {
      newObj[key] = obj[key];
      return newObj;
    }, {});
```

Exemplo de uso:

```js
omit({ a: 1, b: "2", c: 3 }, ["b"]); // { 'a': 1, 'c': 3 }
```
