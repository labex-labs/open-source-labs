# Como Verificar a Igualdade de Objetos em JavaScript

Para verificar se dois valores são equivalentes, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Realize uma comparação profunda (deep comparison) entre os dois valores usando a função `equals()`.
3.  Verifique se os dois valores são idênticos. Se sim, retorne `true`.
4.  Verifique se ambos os valores são objetos `Date` com o mesmo tempo, usando `Date.prototype.getTime()`. Se sim, retorne `true`.
5.  Verifique se ambos os valores são valores não-objeto com um valor equivalente (comparação estrita). Se sim, retorne `true`.
6.  Verifique se apenas um valor é `null` ou `undefined` ou se seus protótipos diferem. Se sim, retorne `false`.
7.  Se nenhuma das condições acima for atendida, use `Object.keys()` para verificar se ambos os valores possuem o mesmo número de chaves.
8.  Use `Array.prototype.every()` para verificar se cada chave em `a` existe em `b` e se elas são equivalentes, chamando `equals()` recursivamente.

Use o seguinte código para implementar a função `equals()`:

```js
const equals = (a, b) => {
  if (a === b) return true;

  if (a instanceof Date && b instanceof Date)
    return a.getTime() === b.getTime();

  if (!a || !b || (typeof a !== "object" && typeof b !== "object"))
    return a === b;

  if (a.prototype !== b.prototype) return false;

  const keys = Object.keys(a);
  if (keys.length !== Object.keys(b).length) return false;

  return keys.every((k) => equals(a[k], b[k]));
};
```

Use os seguintes exemplos de código para testar a função `equals()`:

```js
equals(
  { a: [2, { e: 3 }], b: [4], c: "foo" },
  { a: [2, { e: 3 }], b: [4], c: "foo" }
); // true

equals([1, 2, 3], { 0: 1, 1: 2, 2: 3 }); // true
```
