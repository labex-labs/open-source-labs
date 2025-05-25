# Função para Mapear Valores de Objeto

Para mapear os valores de um objeto usando uma função fornecida para gerar um novo objeto com as mesmas chaves, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use `Object.keys()` para iterar sobre as chaves do objeto.
3. Use `Array.prototype.reduce()` para criar um novo objeto com as mesmas chaves e valores mapeados usando a função fornecida `fn`.
4. O código abaixo demonstra a implementação da função `mapValues`.

```js
const mapValues = (obj, fn) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k] = fn(obj[k], k, obj);
    return acc;
  }, {});
```

Aqui está um exemplo de uso da função `mapValues`:

```js
const users = {
  fred: { user: "fred", age: 40 },
  pebbles: { user: "pebbles", age: 1 }
};
mapValues(users, (u) => u.age); // { fred: 40, pebbles: 1 }
```
