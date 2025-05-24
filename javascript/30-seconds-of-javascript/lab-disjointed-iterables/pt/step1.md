# Verificando Iteráveis Disjuntos

Para verificar se dois iteráveis não possuem valores em comum, você pode usar a função `isDisjoint`.

Veja como usá-la:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Crie um novo objeto `Set` a partir de cada iterável usando o construtor `Set`.
3.  Use `Array.prototype.every()` e `Set.prototype.has()` para verificar se os dois iteráveis não possuem valores em comum.

```js
const isDisjoint = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...sA].every((v) => !sB.has(v));
};
```

Aqui estão alguns exemplos:

```js
isDisjoint(new Set([1, 2]), new Set([3, 4])); // true
isDisjoint(new Set([1, 2]), new Set([1, 3])); // false
```
