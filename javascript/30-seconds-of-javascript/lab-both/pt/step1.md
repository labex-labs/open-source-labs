# Usando o AND Lógico com Funções

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Para verificar se duas funções retornam `true` para um determinado conjunto de argumentos, use o operador AND lógico (`&&`).

```js
const both =
  (f, g) =>
  (...args) =>
    f(...args) && g(...args);
```

O código acima cria uma nova função `both` que recebe duas funções `f` e `g` como entrada e retorna outra função que chama `f` e `g` com os argumentos fornecidos e retorna `true` somente se ambas as funções retornarem `true`.

Por exemplo, para verificar se um número é positivo e par, podemos usar as funções `isEven` e `isPositive` com `both`, conforme mostrado abaixo:

```js
const isEven = (num) => num % 2 === 0;
const isPositive = (num) => num > 0;
const isPositiveEven = both(isEven, isPositive);
isPositiveEven(4); // true
isPositiveEven(-2); // false
```

Aqui, `isPositiveEven` é uma nova função que verifica se um determinado número é positivo e par, usando a função `both` com `isEven` e `isPositive` como entradas.
