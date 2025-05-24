# Como verificar se um objeto está profundamente congelado (Deeply Frozen)

Para verificar se um objeto está profundamente congelado, use as seguintes etapas em JavaScript:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use recursão para verificar se todas as propriedades do objeto estão profundamente congeladas.
3.  Use `Object.isFrozen()` no objeto fornecido para verificar se ele está superficialmente congelado (shallowly frozen).
4.  Use `Object.keys()` para obter todas as propriedades do objeto e `Array.prototype.every()` para verificar se todas as chaves são objetos profundamente congelados ou valores não-objeto.

Aqui está um trecho de código de exemplo para verificar se um objeto está profundamente congelado:

```js
const isDeepFrozen = (obj) =>
  Object.isFrozen(obj) &&
  Object.keys(obj).every(
    (prop) => typeof obj[prop] !== "object" || isDeepFrozen(obj[prop])
  );
```

Você pode usar a função `isDeepFrozen` para verificar se um objeto está profundamente congelado assim:

```js
const x = Object.freeze({ a: 1 });
const y = Object.freeze({ b: { c: 2 } });
isDeepFrozen(x); // true
isDeepFrozen(y); // false
```
