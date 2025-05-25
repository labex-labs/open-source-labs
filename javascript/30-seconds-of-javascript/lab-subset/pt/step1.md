# Verificando se um Subconjunto de um Iterável está Contido em Outro Iterável

Para praticar a codificação, abra o Terminal/SSH e digite `node`. Esta função verifica se o primeiro iterável é um subconjunto do segundo iterável, excluindo valores duplicados.

Para conseguir isso, você pode fazer o seguinte:

- Crie um novo objeto `Set` a partir de cada iterável usando o construtor `Set`.
- Use `Array.prototype.every()` e `Set.prototype.has()` para verificar se cada valor no primeiro iterável está contido no segundo iterável.

Aqui está um exemplo de implementação:

```js
const subSet = (a, b) => {
  const setA = new Set(a);
  const setB = new Set(b);
  return [...setA].every((value) => setB.has(value));
};
```

Você pode usar a função `subSet` passando dois conjuntos para comparar. Por exemplo:

```js
subSet(new Set([1, 2]), new Set([1, 2, 3, 4])); // true
subSet(new Set([1, 5]), new Set([1, 2, 3, 4])); // false
```
