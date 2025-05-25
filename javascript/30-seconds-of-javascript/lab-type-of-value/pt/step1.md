# Função para Obter o Tipo de Valor

Para obter o tipo de um valor, use a seguinte função:

```js
const getType = (v) => {
  if (v === undefined) {
    return "undefined";
  }

  if (v === null) {
    return "null";
  }

  return v.constructor.name;
};
```

- A função retorna `'undefined'` ou `'null'` se o valor for `undefined` ou `null`.
- Caso contrário, ela retorna o nome do construtor usando `Object.prototype.constructor` e `Function.prototype.name`.

Exemplo de uso:

```js
getType(new Set([1, 2, 3])); // 'Set'
```
