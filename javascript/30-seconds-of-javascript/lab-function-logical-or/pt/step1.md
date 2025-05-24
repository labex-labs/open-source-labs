# Usando o "Ou" Lógico para Funções

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

O operador lógico "ou" (`||`) pode ser usado para verificar se pelo menos uma função retorna `true` para um determinado conjunto de argumentos. Para fazer isso, chame as duas funções com os `args` fornecidos e aplique o operador lógico "ou" em seus resultados.

Aqui está um exemplo de implementação da função `either`:

```js
const either =
  (f, g) =>
  (...args) =>
    f(...args) || g(...args);
```

E aqui está um exemplo de uso da função `either` com duas funções `isEven` e `isPositive`:

```js
const isEven = (num) => num % 2 === 0;
const isPositive = (num) => num > 0;
const isPositiveOrEven = either(isPositive, isEven);
isPositiveOrEven(4); // true
isPositiveOrEven(3); // true
```

Neste exemplo, `isPositiveOrEven` retorna `true` tanto para `4` quanto para `3` porque `isEven` retorna `true` para `4` e `isPositive` retorna `true` para `3`.
