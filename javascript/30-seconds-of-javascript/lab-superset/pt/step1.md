# Função para Verificar se um Conjunto é um Superconjunto de Outro Conjunto

Para verificar se um conjunto é um superconjunto de outro conjunto, use a função `superSet()`. Primeiro, abra o Terminal/SSH e digite `node` para começar a praticar a codificação. Em seguida, use as seguintes etapas:

- Crie um novo objeto `Set` a partir de cada iterável usando o construtor `Set`.
- Use `Array.prototype.every()` e `Set.prototype.has()` para verificar se cada valor no segundo iterável está contido no primeiro.
- A função retorna `true` se o primeiro iterável é um superconjunto do segundo, excluindo valores duplicados. Caso contrário, retorna `false`.

```js
const superSet = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...sB].every((v) => sA.has(v));
};
```

Use `superSet()` com dois conjuntos como argumentos para verificar se um conjunto é um superconjunto de outro conjunto.

```js
superSet(new Set([1, 2, 3, 4]), new Set([1, 2])); // true
superSet(new Set([1, 2, 3, 4]), new Set([1, 5])); // false
```
