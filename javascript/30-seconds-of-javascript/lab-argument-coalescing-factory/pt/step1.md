# Código da Fábrica de Coalescência de Argumentos

Para começar a codificar, abra o Terminal/SSH e digite `node`. Esta função retorna o primeiro argumento que avalia para `true` com base no validador passado como um argumento.

```js
const coalesceFactory =
  (validator) =>
  (...args) =>
    args.find(validator);
```

Use `Array.prototype.find()` para retornar o primeiro argumento que retorna `true` da função de validação de argumento fornecida, `valid`. Por exemplo,

```js
const customCoalesce = coalesceFactory(
  (v) => ![null, undefined, "", NaN].includes(v)
);
customCoalesce(undefined, null, NaN, "", "Waldo"); // 'Waldo'
```

Aqui, a função `coalesceFactory` é personalizada para criar a função `customCoalesce`. A função `customCoalesce` filtra `null`, `undefined`, `NaN` e strings vazias dos argumentos fornecidos e retorna o primeiro argumento que não é filtrado. A saída de `customCoalesce(undefined, null, NaN, '', 'Waldo')` é `'Waldo'`.
