# Função para Encontrar a Primeira Chave Correspondente a um Teste

Para encontrar a primeira chave em um objeto que corresponde a uma função de teste fornecida, use a função `findKey()`. Primeiro, obtenha todas as propriedades do objeto usando `Object.keys()`. Em seguida, aplique a função de teste a cada par chave-valor usando `Array.prototype.find()`. A função de teste deve receber três argumentos: o valor, a chave e o objeto. A função retorna a primeira chave que satisfaz a função de teste ou `undefined` se nenhuma for encontrada.

Aqui está um exemplo de implementação de `findKey()`:

```js
const findKey = (obj, fn) =>
  Object.keys(obj).find((key) => fn(obj[key], key, obj));
```

Para usar `findKey()`, passe o objeto e a função de teste como argumentos:

```js
findKey(
  {
    barney: { age: 36, active: true },
    fred: { age: 40, active: false },
    pebbles: { age: 1, active: true }
  },
  (x) => x["active"]
); // 'barney'
```

Neste exemplo, `findKey()` retorna a primeira chave no objeto onde o valor da propriedade `active` é `true`, que é `'barney'`.
