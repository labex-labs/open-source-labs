# Função para Verificar String Sim/Não

Para verificar se uma string é uma resposta `'sim'` ou `'não'`, use a seguinte função no Terminal/SSH digitando `node`:

```js
const yesNo = (val, def = false) =>
  /^(y|yes)$/i.test(val) ? true : /^(n|no)$/i.test(val) ? false : def;
```

- A função retorna `true` se a string for `'y'`/`'yes'` e `false` se a string for `'n'`/`'no'`.
- Para definir uma resposta padrão (default answer), omita o segundo argumento `def`. Por padrão, a função retornará `false`.
- A função usa `RegExp.prototype.test()` para verificar se a string corresponde a `'y'`/`'yes'` ou `'n'`/`'no'`.

Exemplo de uso:

```js
yesNo("Y"); // true
yesNo("yes"); // true
yesNo("No"); // false
yesNo("Foo", true); // true
```
